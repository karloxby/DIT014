
import helper

error_1 = "Error - Value must be greater than zero."
error_2 = "Error - Service code must be S, X or P."

# Give sales staff a consistent quote before they promise a price to a customer.
def calculate_delivery_quote(distance, weight, service_code):
    if service_code == "P":
        service_multiplier = 1.60

    elif service_code == "X":
        service_multiplier = 1.25

    elif service_code == "S":
        service_multiplier = 1.00

    subtotal = 45.00 + distance * 6.50 + weight * 4.00
    quote = subtotal * service_multiplier

    return quote


def main():
    valid_distance = False

    while valid_distance is not True:
        distance_input = input("Distance (km): ")
        distance_input_validated = helper.string_to_float(distance_input)

        if distance_input_validated is not False:
            distance = distance_input_validated

            if distance <= 0:
                print(error_1)
            else:
                valid_distance = True

    valid_weight = False

    while valid_weight is not True:
        weight_input = input("Weight (kg): ")
        weight_input_validated = helper.string_to_float(weight_input)

        if weight_input_validated is not False:
            weight = weight_input_validated

            if weight <= 0:
                print(error_1)
            else:
                valid_weight = True

    valid_service_code = False

    while valid_service_code is not True:
        service_code_input = input("Service code: ").upper()
        
        if service_code_input == "S" or service_code_input == "X" or service_code_input == "P":
            service_code = service_code_input
            valid_service_code = True
        
        else:
            print(error_2)

    quote = calculate_delivery_quote(distance, weight, service_code)
    print(f"Delivery quote: {quote:.2f} SEK")


if __name__ == "__main__":
    main()

