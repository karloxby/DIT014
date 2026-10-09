
import helper

# Give operations management evidence for a Monday performance meeting.
def produce_weekly_dispatch_report(completed_deliveries, daily_target):
    total_deliveries = 0
    days_meeting_target = 0
    
    for delivery in completed_deliveries:
        if delivery >= daily_target:
            days_meeting_target += 1

        total_deliveries += delivery

    average_per_day = f"{total_deliveries / len(completed_deliveries):.2f}"

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    stored_amount = 0
    stored_day = 0
    for day, delivery in enumerate(completed_deliveries):
        if stored_amount <= delivery:
            stored_day = day
            stored_amount = delivery

    highest_day = f"{week[stored_day]} ({completed_deliveries[stored_day]})"
    
    # stored_amount = Highest day, which is the upper bound.
    stored_day = 0
    for day, delivery in enumerate(completed_deliveries):
        if stored_amount >= delivery:
            stored_day = day
            stored_amount = delivery

    lowest_day = f"{week[stored_day]} ({completed_deliveries[stored_day]})"

    return total_deliveries, average_per_day, highest_day, lowest_day, days_meeting_target


def main():
    # Validates completed deliveries are numbers and correct formatting.
    completed_deliveries_validated = False

    while completed_deliveries_validated is not True:
        completed_deliveries = input("Completed deliveries: ")
        completed_deliveries = completed_deliveries.split(",")

        completed_deliveries = helper.strip_spaces(completed_deliveries)

        completed_deliveries_converted = True

        for delivery in completed_deliveries:
            converted_delivery = helper.string_to_int(delivery)
            if (
                converted_delivery is not False
                and converted_delivery >= 0
            ):
                continue
            
            else:
                completed_deliveries_converted = False

        if completed_deliveries_converted is True:
            completed_deliveries = helper.string_to_int(completed_deliveries)

        length_validated = True

        if len(completed_deliveries) != 7:
            print("Error - Weekly report requires 7 delivery counts.")
            length_validated = False

        if completed_deliveries_converted is True and length_validated is True:
               completed_deliveries_validated = True

    while True:
        daily_target = input("Daily target: ")
        converted_daily_target = helper.string_to_int(daily_target)

        if (
            converted_daily_target is not False
            and converted_daily_target >= 0
        ):
            daily_target = converted_daily_target
            break

    (
            total_deliveries, 
            average_per_day, 
            highest_day, 
            lowest_day, 
            days_meeting_target
    ) = produce_weekly_dispatch_report(completed_deliveries, daily_target)

    print("Weekly dispatch report")
    print(f"Total deliveries: {total_deliveries}")
    print(f"Average per day: {average_per_day}")
    print(f"Highest day: {highest_day}")
    print(f"Lowest day: {lowest_day}")
    print(f"Days meeting target: {days_meeting_target}")


if __name__ == "__main__":
    main()

