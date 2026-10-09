
from pathlib import Path

from backend.utils import data_access
from backend.utils import helper
from backend.utils import error


# Give coordinators a trustworthy inventory built from independent JSON records.
def list_registered_vessels():
    directory = Path("backend/dataset/vessels")

    vessels, skipped_vessel_files = load_vessels(directory)
    vessels.sort(key=get_vessel_name)

    return vessels, skipped_vessel_files


def load_vessels(directory):
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

        required_keys = ["vessel_id", "name", "imo", "capacity_teu"]

        vessel, error_message = helper.has_required_keys(vessel, required_keys)

        if vessel is None:
            skip +=1
            print(error_message)
            print(file)
            continue

        if not isinstance(vessel.get("name"), str):
            skip += 1
            print(error.invalid_name)
            print(file)
            continue

        if not isinstance(vessel.get("capacity_teu"), int):
            skip +=1
            print(error.invalid_teu)
            print(file)
            continue

        vessels.append(vessel)

    return vessels, skip


def get_vessel_name(vessel):
    return vessel["name"].lower()


def main():
    vessels, skipped_vessel_files = list_registered_vessels()

    print("Registered HarborFlow vessels:")
    for vessel in vessels:
        print(f"- {vessel["name"]} | IMO {vessel["imo"]} | {vessel["capacity_teu"]:,} TEU")
    print(f"Skipped vessel files: {skipped_vessel_files}")


if __name__ == "__main__":
    main()

