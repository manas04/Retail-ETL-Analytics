from extract import extract_all_raw_data
from transform import transform_all_data
from load import save_processed_data


def main():
    raw_data = extract_all_raw_data()
    print("Raw Dataset extracted successfully")

    cleaned_data = transform_all_data(raw_data)
    print("Data transformed successfully")

    save_processed_data(cleaned_data)
    print('Processed files successfuly saved')

if __name__ == "__main__":
    main()

