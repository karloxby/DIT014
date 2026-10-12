
from backend.utils import operations
from backend.utils import error

from backend.utils import helper


def fetch_data():
    required_keys = ["call_id", "vessel_id", "port_code", "arrival_date"]
    port_calls, skipped_port_call_rows = operations.inspect_port_calls(required_keys)

    required_keys = ["call_id", "vessel_id", "shipment_ids", "event_codes"]
    manifests, skipped_manifest_files = operations.inspect_manifests(required_keys)

    required_keys = ["shipment_id", "customer", "destination", "weight_kg", "priority"]
    shipments, skipped_shipment_files = operations.inspect_shipments(required_keys)

    return port_calls, manifests, shipments


def read_call_id(port_calls):
    call_id = input("Call ID: ")

    call_id = call_id.upper()
    
    call_id, error_message = helper.strip_spaces(call_id)
    # Enforces a specific 12-character ID format.
    '''
    if (
        call_id is None
        or len(call_id) != 12
        or call_id[3] != "-" or call_id[7] != "-"
    ):
        return None, None

    prefix = call_id[0:3]

    if prefix != "HFL":
        return None, None

    customer_code_validated = True
    customer_code = call_id[4:7]

    for character in customer_code:
        character, error_message = helper.string_to_int(character)
        
        if character is not None:
            customer_code_validated = False
            break

    if customer_code_validated is False:
        return None, None
    
    shipment_number_validated = True
    shipment_number = call_id[8:12]

    for number in shipment_number:
        number, error_message = helper.string_to_int(number)

        if number is None:
            shipment_number_validated = False
            break

    if shipment_number_validated is False:
        return None, None
    '''
    matched_port_calls = []
    for port_call in port_calls:
        if call_id.upper() == operations.get_port_call_call_id(port_call).upper():
            matched_port_calls.append(port_call)

    if len(matched_port_calls) == 0:
        return None, None

    return call_id, matched_port_calls


def resolve_shipments(shipment_ids, shipments):
    classified_shipments = []
    for shipment_id in shipment_ids:
        for shipment in shipments:
            if shipment_id == operations.get_shipment_shipment_id(shipment):
                classified_shipments.append(shipment)

    return classified_shipments


def find_manifest(call_id, manifests):
    for manifest in manifests:
        if call_id == operations.get_manifest_call_id(manifest).upper():
            return manifest

    return None


def classify_shipment(shipment):
    # CONTROLLED: hazardous is true.
    if shipment.get("hazardous", False) is True:
        category = "CONTROLLED"
        reason = "hazardous cargo"

    # COLD CHAIN: temperature_controlled is true
    elif shipment.get("temperature_controlled", False) is True:
        category = "COLD CHAIN"
        reason = "temperature controlled cargo"

    # EXPEDITE: priority is EXPRESS or weight_kg >= 5000.
    elif operations.get_shipment_priority(shipment).upper() == "EXPRESS":
        category = "EXPEDITE"
        reason = "express service"

    elif operations.get_shipment_weight_kg(shipment) >= 5000:
        category = "EXPEDITE"
        reason = "weight more than or equal to 5000"

    else:
        category = "STANDARD"
        reason = "standard cargo"

    return category, reason


# Turn raw shipment attributes into a documented operational decision.
def main():
    port_calls, manifests, shipments = fetch_data()
    if (
            port_calls is None
            or manifests is None
            or shipments is None
    ):
        return
    
    # Remark: Remove before submission to CodeGrade.
    for port_call in port_calls:
        print(operations.get_port_call_call_id(port_call))

    call_id, matched_port_calls = read_call_id(port_calls)
    if call_id is None:
        print(error.port_call_not_found)
        return

    target_manifest = find_manifest(call_id, manifests)
    if target_manifest is None:
        print(error.manifest_unavailable)
        return
    
    shipment_ids = operations.get_manifest_shipment_ids(target_manifest)

    classified_shipments = resolve_shipments(shipment_ids, shipments)

    controlled = 0
    cold_chain = 0
    expedite = 0
    standard = 0
    for shipment in classified_shipments:
        shipment_id = operations.get_shipment_shipment_id(shipment)
        category, reason = classify_shipment(shipment)

        if category == "CONTROLLED":
            controlled += 1
        elif category == "COLD CHAIN":
            cold_chain += 1
        elif category == "EXPEDITE":
            expedite += 1
        else:
            standard += 1

        print(f"{shipment_id} | {category} | {reason}")
    
    print(f"Category totals: CONTROLLED={controlled}, COLD CHAIN={cold_chain}, EXPEDITE={expedite}, STANDARD={standard}")


if __name__ == "__main__":
    main()

