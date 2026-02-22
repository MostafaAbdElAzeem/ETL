import os
import pandas as pd

def extract(csv_path=None):
    csv_path = csv_path or "sales_data.csv"
    return pd.read_csv(csv_path)

def transform(df):
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df["total_price"] = df["quantity"] * df["unit_price"]
    df.fillna({"customer_name": "Unknown"}, inplace=True)
    return df

def load(df, output_path=None):
    
    output_path = output_path or "sales_output.csv"
    
    df.to_csv(output_path, index=False)
    return output_path

if __name__ == "__main__":
    data = extract()
    data = transform(data)
    output_file = load(data)
    print(f"ETL process completed successfully! File saved to {output_file}")