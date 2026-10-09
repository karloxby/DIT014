
import helper
import task_3

# Help a sales coordinator compare Standard, Express and Priority quotes before presenting options to a customer.
def compare_delivery_scenarios(distance, weight):
    service_codes = ["S", "X", "P"]
    
    quotes = []
    for service_code in service_codes:
        quote = task_3.calculate_delivery_quote(distance, weight, service_code)
        quotes.append(quote)

    standard = quotes[0]
    express = quotes[1]
    priority = quotes[2]

    service_codes = ["Standard", "Express", "Priority"]

    stored_quote = 0
    stored_service = 0
    for service, quote in enumerate(quotes):
        if stored_quote <= quote:
            stored_service = service
            stored_quote = quote

    most_expensive_service = service_codes[stored_service]

    # stored_quote = Most expensive service, which is the upper bound.
    stored_service = 0
    for service, quote in enumerate(quotes):
        if stored_quote >= quote:
            stored_service = service
            stored_quote = quote

    cheapest_service = service_codes[stored_service]

    return standard, express, priority, cheapest_service, most_expensive_service


def main():
    valid_distance = False

    while valid_distance is not True:
        distance_input = input("Distance (km): ")
        distance_input_validated = helper.string_to_float(distance_input)

        if distance_input_validated is not False:
            distance = distance_input_validated

            if distance <= 0:
                print(task_3.error_1)
            else:
                valid_distance = True

    valid_weight = False

    while valid_weight is not True:
        weight_input = input("Weight (kg): ")
        weight_input_validated = helper.string_to_float(weight_input)

        if weight_input_validated is not False:
            weight = weight_input_validated

            if weight <= 0:
                print(task_3.error_1)
            else:
                valid_weight = True
    
    (
            standard, 
            express, 
            priority, 
            cheapest_service,
            most_expensive_service
    ) = compare_delivery_scenarios(distance, weight)

    print("Service comparison")
    print(f"Standard: {standard:.2f} SEK")
    print(f"Express: {express:.2f} SEK")
    print(f"Priority: {priority:.2f} SEK")
    print(f"Cheapest service: {cheapest_service}")
    print(f"Most expensive service: {most_expensive_service}")


if __name__ == "__main__":
    main()

