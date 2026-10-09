
# Give dispatchers one dependable entry point to every service.
def console():
    console_title = "Harborflow Dispatch Console"
    console_options = [
        "1. Close console", 
        "2. Validate booking reference",
        "3. Calculate delivery quote",
        "4. Consolidate parcel labels",
        "5. Check van capacity",
        "6. Classify service performance",
        "7. Produce weekly dispatch report",
        "8. Compare service scenarios"
    ]

    print(console_title.upper())
    for option in console_options:
        print(option)

    return input("Select service: ")


def main():
    console()


if __name__ == "__main__":
    main()

