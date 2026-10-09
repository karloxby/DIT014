
# Give dispatchers one dependable entry point to every service.
def validate_reference(reference):
    stripped_reference = reference.strip()

    if len(stripped_reference) != 12:
        reference = ""
        return reference

    if stripped_reference[3] != "-" or stripped_reference[7] != "-":
        reference = ""
        return reference

    fixed_prefix = stripped_reference[0:3].upper()
    customer_code = stripped_reference[4:7].upper()
    shipment_number = stripped_reference[8:12]

    template_prefix = "HFL"

    if fixed_prefix != template_prefix:
        reference = ""
        return reference

    characters = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    for char in customer_code:
        if char not in characters:
            reference = ""
            return reference

    for number in shipment_number:
        try:
            number = int(number)
            continue
        except ValueError:
            reference = ""
            return reference

    shipment_number = str(shipment_number)

    reference = fixed_prefix + "-" + customer_code + "-" + shipment_number

    return reference


def main():
    reference_input = input("Booking reference: ")
    reference = validate_reference(reference_input)

    if reference == "":
        print("Invalid booking reference.")
    else:
        print(f"Valid reference: {reference}")


if __name__ == "__main__":
    main()

