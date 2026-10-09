
import helper

error = "Error - Value must be greater than zero."

# Translate operational numbers into a consistent customer service status.
def classify_service_performance(promised_minutes, actual_minutes, damaged_parcels):
    delay = actual_minutes - promised_minutes

    if delay <= 0:
        service_status = "On time".upper()
    elif delay <= 15:
        service_status = "Minor delay".upper()
    else:
        service_status = "Major delay".upper()

    if damaged_parcels > 0:
        service_status = "Service failure".upper()

    return delay, service_status


def main():
    while True:
        promised_minutes = input("Promised minutes: ")
        promised_minutes = helper.string_to_int(promised_minutes)

        if promised_minutes is not False and promised_minutes >= 0:
            break
        
    while True:
        actual_minutes = input("Actual minutes: ")
        actual_minutes = helper.string_to_int(actual_minutes)

        if actual_minutes is not False and actual_minutes >= 0:
            break

    while True:
        damaged_parcels = input("Damaged parcels: ")
        damaged_parcels = helper.string_to_int(damaged_parcels)
        
        if damaged_parcels is not False and damaged_parcels >= 0:
            break

    delay, service_status = classify_service_performance(promised_minutes, actual_minutes, damaged_parcels)
    
    print(f"Delay: {delay} minutes")
    print(f"Service status: {service_status}")

if __name__ == "__main__":
    main()

