
def main():
    menu = [
        "1. List registered vessels",
        "2. Inspect a vessel manifest",
        "3. Identify priority cargo",
        "4. Export a customer operations profile",
        "5. Find port calls by month",
        "6. Sanitize an incident report",
        "7. Analyze the longest stable event sequence",
        "8. Assess weather risk for upcoming calls",
        "9. Search incident reports",
        "10. Close console",
    ]

    print("HARBORFLOW PORT INTELLIGENCE")
    for option in menu:
        print(option)

    return input("Select service: ")


if __name__ == "__main__":
    main()
