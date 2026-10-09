
import random

weeks = []

# Converts to int: Accepts list or str
def string_to_int(target):
    if type(target) == list:
        converted_target = []

        for item in target:
            try:
                item = int(item)
                converted_target.append(item)
            except ValueError:
                return "Exit code 1 - Item in target list cannot be turned to int."

        target = converted_target

    elif type(target) == str:
        try:
            target = int(target)
        except ValueError:
            return "Exit code 1 - Target string cannot be turned to int."
        
    else:
        return "Exit code 1 - Target must be a string or list."

    return target


def menu():
    menu = ["Add a week", "Show weekly summaries", "Exit"]

    print("\nGATHERGRID PARTICIPATION TRACKER")
    for index, option in enumerate(menu, 1):
        print(f"{index}. {option}")

    choice = string_to_int(input("\nChoice: "))

    if type(choice) != str:
        return choice
    else:
        print(choice)


def add_a_week():
    week = []

    while True:
        random_toggle = input("\nToggle randomizer (y)/(n): ").lower()

        if random_toggle == "n":
            randomizer = False
            break
        elif random_toggle == "y":
            randomizer = True
            break
        else:
            print("Must be (y)es or (n)o.")
    
    # For manual input
    if randomizer is False:
        for day in range(1, 8):
            while True:
                morning = string_to_int(input(f"Day {day} morning: "))

                if type(morning) != str and morning >= 0:
                    break
            
            while True:
                afternoon = string_to_int(input(f"Day {day} afternoon: "))

                if type(afternoon) != str and afternoon >= 0:
                    break

            while True:
                evening = string_to_int(input(f"Day {day} evening: "))

                if type(evening) != str and evening >= 0:
                    break
        
            week.append((day, [morning, afternoon, evening]))
    
    # For randomizer
    else:
        for day in range(1, 8):
            morning = random.randint(4, 16)
            print(f"Day {day} morning: {morning}")
            afternoon = random.randint(4, 16)
            print(f"Day {day} afternoon: {afternoon}")
            evening = random.randint(4, 16)
            print(f"Day {day} evening: {evening}")

            week.append((day, [morning, afternoon, evening]))

    weeks.append(week)


def show_weekly_summaries():
    for week, days in enumerate(weeks, 1):
        total_participation = 0
        highest_day = 0
        highest_participation = 0

        for day in days:
            current_total = sum(day[1])
            total_participation += current_total

            if current_total >= highest_participation:
                highest_day = day[0]
                highest_participation = current_total
        
        # Because 3 records per day \times 7 days is 21.
        average = total_participation / 21
        print(f"\nWeek {week}")
        print(f"Average participation: {average:.2f}")
        print(f"Highest participation: Day {highest_day} ({highest_participation})")


def main():
    while True:
        choice = menu()

        if choice == 1:
            add_a_week()
        elif choice == 2:
            show_weekly_summaries()
        elif choice == 3:
            break
        else:
            print("Select 1 through 3 from the menu.")


if __name__ == "__main__":
    main()
