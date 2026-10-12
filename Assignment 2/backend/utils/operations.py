
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

        if not isinstance(vessel.get("name"), str):
            skip += 1
            print(error.invalid_name)
            print(file)
            continue

        if not isinstance(vessel.get("capacity_teu"), int):
            skip += 1
            print(error.invalid_teu)
            print(file)
            continue

        vessels.append(vessel)

    return vessels, skip


def get_vessel_name(vessel):
    return vessel["name"].lower()


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

        if not isinstance(manifest.get("shipment_ids"), list):
            skip += 1
            print(error.invalid_ids)
            print(file)
            continue

        if not isinstance(manifest.get("event_codes"), list):
            skip += 1
            print(error.invalid_codes)
            print(file)
            continue

        manifests.append(manifest)

    return manifests, skip


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


def get_arrival_date(port_call):
    return port_call["arrival_date"]


def get_call_id(port_call):
    return port_call["call_id"]


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

        if type(shipment.get("weight_kg")) not in (int, float):
            skip += 1
            print(error.weight_kg)
            print(file)
            continue

        shipments.append(shipment)

    return shipments, skip


def get_shipment_id(shipment):
    return shipment["shipment_id"]

