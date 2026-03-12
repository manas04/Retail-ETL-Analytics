import pandas as pd

def clean_train(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    #Fill missing sales with 0
    df['sales'] = df['sales'].fillna(0)

    #Fill missing on-promotion with 0
    df['onpromotion'] = df['onpromotion'].fillna(0)

    # Drop duplicates from the data
    df = df.drop_duplicates()

    return df

def clean_stores(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.drop_duplicates()
    return df

def clean_transactions(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['transactions'] = df['transactions'].fillna(0)
    df = df.drop_duplicates()
    return df

def transform_all_data(data: dict) -> dict:
    transformed_data = {
        "train": clean_train(data["train"]),
        "stores": clean_stores(data["stores"]),
        "transactions": clean_transactions(data["transactions"]),
    }

    return transformed_data

# df = pd.read_csv('/Users/manas/Desktop/ETL Projects/pricing-etl-kaggle/data/raw/transactions.csv')
# print(df.head(10))
