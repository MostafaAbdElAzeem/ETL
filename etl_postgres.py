import os
import pandas as pd
from sqlalchemy import create_engine

def extract(csv_path=None):
    csv_path = csv_path or  "sales_data.csv"
    return pd.read_csv(csv_path)

def transform(df):
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df["total_price"] = df["quantity"] * df["unit_price"]
    df.fillna({"customer_name": "Unknown"}, inplace=True)
    return df

def load(df, engine_url=None):
    engine_url = engine_url or (
        f"postgresql+psycopg2://{os.getenv('DB_USER','postgres')}:"
        f"{os.getenv('DB_PASSWORD','postgres')}@"
        f"{os.getenv('DB_HOST','localhost')}:"
        f"{os.getenv('DB_PORT','5432')}/"
        f"{os.getenv('DB_NAME','postgres')}"
    )
    engine = create_engine(engine_url)
    df.to_sql("sales", engine, if_exists="replace", index=False)
    return engine

if __name__ == "__main__":
    data = extract()
    data = transform(data)
    load(data)
    print("ETL process completed successfully!")