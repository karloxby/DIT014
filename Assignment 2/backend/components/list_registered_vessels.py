
from backend.utils import operations


# Give coordinators a trustworthy inventory built from independent JSON records.
def main():
    required_keys = ["vessel_id", "name", "imo", "capacity_teu"]

    vessels, skipped_vessel_files = operations.inspect_vessels(required_keys)

    print("Registered HarborFlow vessels:")
    for vessel in vessels:
        print(f"- {vessel['name']} | IMO {vessel['imo']} | {vessel['capacity_teu']:,} TEU")
    print(f"Skipped vessel files: {skipped_vessel_files}")


if __name__ == "__main__":
    main()

