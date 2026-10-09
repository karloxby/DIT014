
from pathlib import Path

from backend.utils import data_access
from backend.utils import helper
from backend.utils import error

from backend.components import list_registered_vessels


# Connect a scheduled port call to its vessel and cargo instead of reading files in isolation.
def inspect_vessel_manifest():
    directory = Path("backend/dataset/manifests")

    manifests, skipped_manifest_files = load_manifests(directory)

    return manifests, skipped_manifest_files


def load_manifests(directory):
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

        required_keys = ["call_id", "vessel_id", "shipment_ids", "event_codes"]

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
            skip+= 1
            print(error.invalid_codes)
            print(file)
            continue

        manifests.append(manifest)

    return manifests, skip


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
        print("Error - Could not find a match.")
        return None

    return vessel


def main():
    manifests, skipped_manifest_files = inspect_vessel_manifest()
    vessels, skipped_vessel_files = list_registered_vessels.list_registered_vessels()

    vessel = registered_vessels(vessels)

    if vessel != None:
        print(vessel)


if __name__ == "__main__":
    main()

