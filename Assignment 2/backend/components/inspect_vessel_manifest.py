
from backend.utils import error

from backend.utils import helper
from backend.utils import operations


def registered_vessels(vessels):
    while True:
        vessel_name = input("Vessel name: ")

        vessel_name, error_message = helper.strip_spaces(vessel_name)

        if vessel_name is not None:
            vessel_name = vessel_name.lower()
            break

        else:
            print(error_message)
    
    vessel_index = None
    for index, vessel in enumerate (vessels):
        if vessel_name == vessel.get("name").lower():
            vessel_index = index

    if vessel_index is not None:
        vessel = vessels[vessel_index]

    else:
        return None, None

    while True:
        reference_date = input("Reference date: ")

        reference_date, error_message = helper.strip_spaces(reference_date)
        error_message = error.date_format

        if reference_date is None:
            print(error_message)
            continue

        reference_date, error_message = helper.validate_date(reference_date)

        if reference_date is None:
            print(error_message)
            continue

        else:
            break

    return vessel, reference_date


def get_earliest_call(port_calls, vessel, reference_date):
    vessel_port_calls = []
    for port_call in port_calls:
        if port_call.get("vessel_id") == vessel.get("vessel_id"):
            vessel_port_calls.append(port_call)

    # Important: Otherwise, select first qualifying port call, not necessarily the earliest.
    vessel_port_calls.sort(key=operations.get_call_id)
    vessel_port_calls.sort(key=operations.get_arrival_date)
    
    earliest_call = None
    for port_call in vessel_port_calls:
        arrival_date, error_message = helper.validate_date(operations.get_arrival_date(port_call))
    
        if arrival_date is None:
            continue

        if arrival_date >= reference_date:
            earliest_call = port_call
            break

    return earliest_call


def identify_manifest(manifests, earliest_call):
    for manifest in manifests:
        if operations.get_call_id(earliest_call) == operations.get_call_id(manifest):
            return manifest

    return None


def get_shipment_records(shipment_ids, shipments):
    shipment_records = []

    for shipment in shipments:
        if shipment.get("shipment_id") in shipment_ids:
            shipment_records.append(shipment)

    return shipment_records


# Connect a scheduled port call to its vessel and cargo instead of reading files in isolation.
def main():
    # Find vessel.
    required_keys = ["vessel_id", "name", "imo", "capacity_teu"]
    vessels, skipped_vessel_files = operations.inspect_vessels(required_keys)

    print("Registered HarborFlow vessels.")
    for vessel in vessels:
        print(f"- {vessel.get('name')} | {vessel.get('vessel_id')}")
    
    vessel, reference_date = registered_vessels(vessels)
    if vessel is None:
        print(error.vessel_not_found)
        return
    
    # Find earliest call.
    required_keys = ["arrival_date", "call_id", "port_code", "vessel_id"]
    port_calls, skipped_port_call_rows = operations.inspect_port_calls(required_keys)
    if port_calls is None:
        return

    earliest_call = get_earliest_call(port_calls, vessel, reference_date)
    if earliest_call is None:
        print(error.no_qualifying_call)
        return
    
    # Identify manifest.
    required_keys = ["call_id", "vessel_id", "shipment_ids", "event_codes"]
    manifests, skipped_manifest_files = operations.inspect_manifests(required_keys)

    identified_manifest = identify_manifest(manifests, earliest_call)
    if identified_manifest is None:
        print(error.manifest_not_found)
        return

    arrival_date, error_message = helper.validate_date(operations.get_arrival_date(earliest_call))
    arrival_date = arrival_date.strftime("%d %B %Y")
        
    print(f"Manifest for {vessel.get("name")} | Call {earliest_call.get("call_id")} | {arrival_date}")

    shipment_ids = identified_manifest.get("shipment_ids")
    
    # Find shipments.
    required_keys = ["shipment_id", "customer", "destination", "weight_kg", "priority"]
    shipments, skipped_shipment_files = operations.inspect_shipments(required_keys)
    if shipments is None:
        return

    shipment_records = get_shipment_records(shipment_ids, shipments)

    declared_shipments = len(shipment_ids)
    resolved_weight = 0
    missing_shipment_records = 0
    for listing, shipment_id in enumerate(shipment_ids, 1):
        identified_shipment = None

        for shipment in shipment_records:
            if operations.get_shipment_id(shipment) == shipment_id:
                identified_shipment = shipment
                resolved_weight += shipment.get("weight_kg")
                break

        if identified_shipment is None:
            print(f"{listing}. {shipment_id} | MISSING RECORD")
            missing_shipment_records += 1

        else:
            print(f"{listing}. {shipment_id} | {identified_shipment.get('customer')} | {float(identified_shipment.get('weight_kg')):.1f} kg | {identified_shipment.get('cargo_type', 'NOT PROVIDED')}")
    
    print(f"Declared shipments: {declared_shipments}")
    print(f"Resolved weight: {float(resolved_weight):.2f} kg")
    print(f"Missing shipment records: {missing_shipment_records}")
    

if __name__ == "__main__":
    main()

