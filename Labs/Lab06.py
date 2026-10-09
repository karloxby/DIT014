total = 0
count = 0

items = ["Coffee", "Sandwich", "Cake"]
prices = [25, 45, 35]


def menu(items, prices):
    print("")

    for index in range(len(items)):
        price = str(prices[index]) + " SEK"
        print(f"{index + 1:<8} {items[index]:<16} {price:>8}")

    print(f"{'0':<8} {'Finish order':<16} {'—':>8}")


def choices(choice, total, count):
    while choice != "0":
        if choice == "1":
            total += prices[0]
            count += 1

        elif choice == "2":
            total += prices[1]
            count += 1

        elif choice == "3":
            total += prices[2]
            count += 1

        else:
            print("\nError - Must be valid choices in the menu.")

        choice = input("\nChoice:\n")

    return total, count


def calc_discount(total):
    if total >= 100:
        discount = total * 0.10
    elif total < 100 and total == 50:
        discount = discount * 0.05
    else:
        discount = 0

    subtotal = round(float(total), 2)
    total = round(float(subtotal - discount), 2)

    subtotal = str(subtotal) + " SEK"
    discount = str(discount) + " SEK"
    total = str(total) + " SEK"

    return subtotal, discount, total


menu(items, prices)
total, count = choices(input("\nChoice:\n"), total, count)
subtotal, discount, total = calc_discount(total)

print(f"\nItems: {count}")
print(f"{'Subtotal':.<16}{subtotal:.>16}")
print(f"{'Discount':.<16}{discount:.>16}")
print(f"{'Total':.<16}{total:.>16}\n")

