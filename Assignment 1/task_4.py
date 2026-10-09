
# Turn duplicate scan data into a clean loading list without losing operational order.
def consolidate_parcel_labels(scanned_labels):
    parsed_scanned_labels = ""

    for char in scanned_labels:
        parsed_scanned_labels += char.upper()

    scanned_labels = parsed_scanned_labels.split(",")
    
    parsed_scanned_labels = []

    for label in scanned_labels:
        parsed_scanned_labels.append(label.strip())

    scanned_labels = parsed_scanned_labels
    
    unique_load_list = []

    for label in scanned_labels:
        if label not in unique_load_list:
            unique_load_list.append(label)
        else:
            continue

    return unique_load_list, len(unique_load_list)


def main():
    scanned_labels = input("Scanned labels: ")
    unique_load_list, total_unique_parcels = consolidate_parcel_labels(scanned_labels)

    print("Unique load list:")
    for parcel in range(len(unique_load_list)):
        print(f"{parcel + 1}. {unique_load_list[parcel]}")

    print(f"Total unique parcels: {total_unique_parcels}")


if __name__ == "__main__":
    main()

