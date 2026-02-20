import os
import pandas as pd
from sqlalchemy import create_engine

# Read environment variables (with defaults)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

# Extract
data = pd.read_csv(os.getenv("CSV_FILE_PATH", "sales_data.csv"))

# Transform
data.drop_duplicates(inplace=True)
data["total_price"] = data["quantity"] * data["unit_price"]
data.fillna({"customer_name": "Unknown"}, inplace=True)

# Load
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

data.to_sql("sales", engine, if_exists="replace", index=False)

print("ETL process completed successfully!")