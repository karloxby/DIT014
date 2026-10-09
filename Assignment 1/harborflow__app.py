
import helper
import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7
import task_9


def main():
    dispatch_menu = True

    while dispatch_menu is True:
        service_input = task_1.console()
        
        # Close menu
        if helper.string_to_int(service_input) == 1:
            print("Console closed. Dispatch data remains safe.")
            dispatch_menu = False

        # Validate booking reference
        elif helper.string_to_int(service_input) == 2:
            task_2.main()
        
        # Calculate delivery quote
        elif helper.string_to_int(service_input) == 3:
            task_3.main()

        # Consolidate parcel labels
        elif helper.string_to_int(service_input) == 4:
            task_4.main()

        # Check van capacity
        elif helper.string_to_int(service_input) == 5:
            task_5.main()

        # Classify service performance
        elif helper.string_to_int(service_input) == 6:
            task_6.main()

        # Produce weekly dispatch report
        elif helper.string_to_int(service_input) == 7:
            task_7.main()

        # Compare service scenarios
        elif helper.string_to_int(service_input) == 8:
            task_9.main()

        else:
            print("Error - Select a service from 1 to 8.")


if __name__ == "__main__":
    main()

