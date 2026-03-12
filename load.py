import os

def save_processed_data(data: dict, output_path: str = '../data/processed') -> None:
    os.makedirs(output_path, exist_ok=True)

    for name, df in data.items():
        file_path = os.path.join(output_path, f"{name}_cleaned.csv")
        df.to_csv(file_path, index=False)
        print(f"Saved {name} to {file_path}")

        