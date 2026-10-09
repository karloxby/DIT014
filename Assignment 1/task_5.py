
import helper

# Help a dispatcher accept as many parcels as possible without overloading a vehicle.
def check_van_capacity(van_capacity, parcel_weights):
    accepted_parcels = 0
    loaded_weight = 0
    remaining_capacity = van_capacity

    for parcel, weight in enumerate(parcel_weights, 1):
        if weight <= remaining_capacity:
            loaded_weight += weight
            accepted_parcels += 1
            remaining_capacity = remaining_capacity - weight
            print(f"Parcel {parcel}: ACCEPTED")

        else:
            print(f"Parcel {parcel}: REJECTED")

    return accepted_parcels, loaded_weight, remaining_capacity


def main():
    # Validates van vapacity is a number greater than 0.
    while True:
        van_capacity = input("Van capacity (kg): ")
        van_capacity = helper.string_to_float(van_capacity)

        if (
                van_capacity is not False
                and van_capacity > 0
        ):
            break
        else:
            print("Error - Value must be greater than zero.")
    
    # Validates parcel weights are numbers greater than 0 and correct formatting.
    parcel_weights_validated = False

    while parcel_weights_validated is not True:
        parcel_weights = input("Parcel weights (kg): ")
        parcel_weights = parcel_weights.split(",")

        parcel_weights = helper.strip_spaces(parcel_weights)

        parcel_weights_converted = True

        for parcel in parcel_weights:
            converted_parcel = helper.string_to_float(parcel)
            if (
                    converted_parcel is not False 
                    and converted_parcel > 0
            ):
                continue

            else:
                parcel_weights_converted = False

        if parcel_weights_converted is True:
            parcel_weights = helper.string_to_float(parcel_weights)
            parcel_weights_validated = True

        else:
            print("Error - Value must be greater than zero.")

    accepted_parcels, loaded_weight, remaining_capacity = check_van_capacity(van_capacity, parcel_weights)
    print(f"Accepted parcels: {accepted_parcels}")
    print(f"Loaded weight: {loaded_weight:.2f} kg")
    print(f"Remaining capacity: {remaining_capacity:.2f} kg")


if __name__ == "__main__":
    main()

