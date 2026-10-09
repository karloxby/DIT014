
from frontend import menu

from backend.utils import helper
from backend.utils import error

from backend.components import (
        list_registered_vessels,
        inspect_vessel_manifest,
        task_3,
        task_4,
        task_5,
        task_6,
        task_7,
        task_8,
        task_9
)


def main():
    console = True
    while console is True:
        service = menu.main()

        valid_service = False
        service = helper.string_to_int(service)

        if service is not None:
            valid_service = True
        else:
            print(error.invalid_service)

        if valid_service is True:
            # List registered vessels
            if service == 1:
                list_registered_vessels.main()
            # Inspect a vessel manifest
            elif service == 2:
                inspect_vessel_manifest.main()
            # Identify priority cargo
            elif service == 3:
                task_3.main()
            # Export a customer operations profile
            elif service == 4:
                task_4.main()
            # Find port calls by month
            elif service == 5:
                task_5.main()
            # Sanitize an incident report
            elif service == 6:
                task_6.main()
            # Analyze the longest stable event sequence
            elif service == 7:
                task_7.main()
            # Assess weather risk for upcoming calls
            elif service == 8:
                task_8.main()
            # Search incident reports
            elif service == 9:
                task_9.main()
            # Close console
            elif service == 10:
                print("Console closed. HarborFlow operational data remains safe.")
                console = False
            else:
                print(error.invalid_service)


if __name__ == "__main__":
    main()

