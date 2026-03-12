import pandas as pd
import os

def extract_csv(filepath:str):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'file not found {filepath}')
    df = pd.read_csv(filepath)
    print(f'Loaded {filepath} with shape: {df.shape}')

    return df

def extract_all_raw_data(base_path: str = '../data/raw') -> dict:
    files = {
    "train": "train.csv",
    "stores": "stores.csv",
    "transactions": "transactions.csv",
    "oil": "oil.csv",
    "holidays": "holidays_events.csv"
}
    data = {}

    for key, filename in files.items():
        full_path = os.path.join(base_path, filename)
        data[key] = extract_csv(full_path)

    return data


