menu_options = ["1. View products", "2. Make an order", "3. Finish"]

products = ["Notebook", "Mug", "Tote bag"]
prices = [40, 60, 80]


def show_products(products, prices):
    print("\nAVAILABLE PRODUCTS")

    index = 0
    while index < len(products):
        print(f"{index + 1}. {products[index]} - {prices[index]} SEK")
        index += 1

    print("\nReturning to menu...")


def make_order(products, prices):
    print("\nMAKE AN ORDER")
    print("Enter 0 when you are finished ordering.")

    subtotal = 0
    items = 0
    discount = 0

    make_order_menu = True

    while make_order_menu is True:
        product = int(input("\nProduct:\n"))

        if product == 1:
            quantity = int(input("Quantity:\n"))

            total = prices[0] * quantity
            subtotal += prices[0] * quantity
            items += quantity

            if quantity >= 5:
                discount = 0.10

            print(f"\n{products[0]} x{quantity}: {total} SEK\n")

        elif product == 2:
            quantity = int(input("Quantity:\n"))

            total = prices[1] * quantity
            subtotal += prices[1] * quantity
            items += quantity

            if quantity >= 5:
                discount = 0.10

            print(f"\n{products[1]} x{quantity}: {total} SEK\n")

        elif product == 3:
            quantity = int(input("Quantity:\n"))

            total = prices[2] * quantity
            subtotal += prices[2] * quantity
            items += quantity

            if quantity >= 5:
                discount = 0.10

            print(f"\n{products[2]} x{quantity}: {total} SEK\n")
        
        elif product == 0:
            make_order_menu = False
        
        else:
            print("\nError - Must be an available product\n")
    
    print("\nReturning to menu...")

    return subtotal, items, discount


def finish_order(subtotal, items, discount):
    print("\nLANTERN POP-UP RETAIL")

    if discount == 0.10:
        discount = subtotal * discount
        total = subtotal - discount

        print(f"Items: {items}")
        print(f"Subtotal{subtotal:.>16.2f} SEK")
        print(f"Discount{discount:.>16.2f} SEK")
        print(f"Total{total:.>16.2f} SEK")

    else:
        print(f"Items: {items}")
        print(f"Subtotal{subtotal:.>16.2f} SEK")
        print(f"Discount{'0.00':.>16} SEK")
        print(f"Total{total:.>16.2f} SEK\n")

    print("\nThank you!\n")


def main(menu_options):
    menu = True

    while menu is True:
        print("\nLANTERN POP-UP RETAIL")
        for option in menu_options:
            print(option)

        user_input = int(input("\nChoice:\n"))

        if user_input == 1:
            show_products(products, prices)

        elif user_input == 2:
            subtotal, items, discount = make_order(products, prices)

        elif user_input == 3:
            finish_order(subtotal, items, discount)
            menu = False

        else:
            print("\nError - Must be a choice from the menu\n")


if __name__ == "__main__":
    main(menu_options)

