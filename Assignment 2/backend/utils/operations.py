
from pathlib import Path

from backend.utils import data_access
from backend.utils import error

from backend.utils import helper


# Get backend/dataset/vessels/*.json
def inspect_vessels(required_keys):
    directory = Path("backend/dataset/vessels")

    vessels, skipped_vessel_files = load_vessels(directory, required_keys)
    vessels.sort(key=get_vessel_name)

    return vessels, skipped_vessel_files


def load_vessels(directory, required_keys):
    vessels = []
    skip = 0

    for file in directory.glob("*.json"):
        vessel, error_message = data_access.load_json(file)

        if vessel is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        keys, error_message = helper.get_keys(vessel)

        if keys is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        vessel, error_message = helper.has_required_keys(vessel, required_keys)

        if vessel is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        if "vessel_id" in required_keys:
            if not isinstance(vessel.get("vessel_id"), str):
                skip += 1
                print(error.invalid_vessel_id)
                print(file)
                continue
        
        if "name" in required_keys:
            if not isinstance(vessel.get("name"), str):
                skip += 1
                print(error.invalid_name)
                print(file)
                continue
        
        if "imo" in required_keys:
            if not isinstance(vessel.get("imo"), int):
                skip += 1
                print(error.invalid_imo)
                print(file)
                continue

        if "capacity_teu" in required_keys:
            if not isinstance(vessel.get("capacity_teu"), int):
                skip += 1
                print(error.invalid_teu)
                print(file)
                continue

        vessels.append(vessel)

    return vessels, skip


def get_vessel_id(vessel):
    return vessel["vessel_id"]

def get_vessel_name(vessel):
    return vessel["name"].lower()

def get_vessel_imo(vessel):
    return vessel["imo"]

def get_vessel_capacity_teu(vessel):
    return vessel["capacity_teu"]


# Get backend/dataset/manifests/*.json
def inspect_manifests(required_keys):
    directory = Path("backend/dataset/manifests")

    manifests, skipped_manifest_files = load_manifests(directory, required_keys)

    return manifests, skipped_manifest_files


def load_manifests(directory, required_keys):
    manifests = []
    skip = 0

    for file in directory.glob("*.json"):
        manifest, error_message = data_access.load_json(file)

        if manifest is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        keys, error_message = helper.get_keys(manifest)

        if keys is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        manifest, error_message = helper.has_required_keys(manifest, required_keys)

        if manifest is None:
            skip += 1
            print(error_message)
            print(file)
            continue
        
        if "call_id" in required_keys:
            if not isinstance(manifest.get("call_id"), str):
                skip += 1
                print(error.invalid_call_id)
                print(file)
                continue

        if "vessel_id" in required_keys:
            if not isinstance(manifest.get("vessel_id"), str):
                skip += 1
                print(error.invalid_vessel_id)
                print(file)
                continue
        
        if "shipment_ids" in required_keys:
            if not isinstance(manifest.get("shipment_ids"), list):
                skip += 1
                print(error.invalid_ids)
                print(file)
                continue
        if "event_codes" in required_keys:
            if not isinstance(manifest.get("event_codes"), list):
                skip += 1
                print(error.invalid_codes)
                print(file)
                continue

        manifests.append(manifest)

    return manifests, skip


def get_manifest_call_id(manifest):
    return manifest["call_id"]

def get_manifest_vessel_id(manifest):
    return manifest["vessel_id"]

def get_manifest_shipment_ids(manifest):
    return manifest["shipment_ids"]

def get_manifest_event_codes(manifest):
    return manifest["event_codes"]


# Get backend/dataset/port_calls.csv
def inspect_port_calls(required_keys):
    path = Path("backend/dataset/port_calls.csv")

    port_calls, skipped_port_call_rows = load_port_calls(path, required_keys)

    return port_calls, skipped_port_call_rows


def load_port_calls(path, required_keys):
    port_calls = []
    skip = 0

    port_call, error_message = data_access.load_csv(path)

    if port_call is None:
        print(error_message)
        return None, None

    for call in port_call:
        keys, error_message = helper.get_keys(call)

        if keys is None:
            skip += 1
            print(error_message)
            continue

        call, error_message = helper.has_required_keys(call, required_keys)

        if call is None:
            skip += 1
            print(error_message)
            continue

        port_calls.append(call)

    return port_calls, skip


def get_port_call_call_id(port_call):
    return port_call["call_id"]

def get_port_call_vessel_id(port_call):
    return port_call["vessel_id"]

def get_port_call_port_code(port_call):
    return port_call["port_code"]

def get_port_call_arrival_date(port_call):
    return port_call["arrival_date"]


# Get backend/dataset/shipments/*.json
def inspect_shipments(required_keys):
    directory = Path("backend/dataset/shipments")

    shipments, skipped_shipment_files = load_shipments(directory, required_keys)

    return shipments, skipped_shipment_files


def load_shipments(directory, required_keys):
    shipments = []
    skip = 0

    for file in directory.glob("*.json"):
        shipment, error_message = data_access.load_json(file)

        if shipment is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        keys, error_message = helper.get_keys(shipment)

        if keys is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        shipment, error_message = helper.has_required_keys(shipment, required_keys)

        if shipment is None:
            skip += 1
            print(error_message)
            print(file)
            continue

        if "shipment_id" in required_keys:
            if not isinstance(shipment.get("shipment_id"), str):
                skip += 1
                print(error.invalid_shipment_id)
                print(file)
                continue

        if "customer" in required_keys:
            if not isinstance(shipment.get("customer"), str):
                skip += 1
                print(error.invalid_customer)
                print(file)
                continue

        if "destination" in required_keys:
            if not isinstance(shipment.get("destination"), str):
                skip += 1
                print(error.invalid_destination)
                print(file)
                continue
        
        if "weight_kg" in required_keys:
            if type(shipment.get("weight_kg")) not in (int, float):
                skip += 1
                print(error.weight_kg)
                print(file)
                continue

        if "priority" in required_keys:
            if not isinstance(shipment.get("priority"), str):
                skip += 1
                print(error.invalid_priority)
                print(file)
                continue

        if "hazardous" in required_keys:
            if not isinstance(shipment.get("hazardous"), bool):
                skip += 1
                print(error.invalid_hazardous)
                print(file)
                continue

        if "temperature_controlled" in required_keys:
            if not isinstance(shipment.get("temperature_controlled"), bool):
                skip += 1
                print(error.invalid_temperature_controlled)
                print(file)
                continue

        if "cargo_type" in required_keys:
            if not isinstance(shipment.get("cargo_type"), str):
                skip += 1
                print(error.invalid_cargo_type)
                print(file)
                continue

        shipments.append(shipment)

    return shipments, skip


def get_shipment_shipment_id(shipment):
    return shipment["shipment_id"]

def get_shipment_customer(shipment):
    return shipment["customer"]

def get_shipment_destination(shipment):
    return shipment["destination"]

def get_shipment_weight_kg(shipment):
    return shipment["weight_kg"]

def get_shipment_priority(shipment):
    return shipment["priority"]

def get_shipment_hazardous(shipment):
    return shipment["hazardous"]

def get_shipment_temperature_controlled(shipment):
    return shipment["temperature_controlled"]

def get_shipment_cargo_type(shipment):
    return shipment["cargo_type"]

