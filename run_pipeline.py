import os
import pandas as pd
from dotenv import load_dotenv
from scripts.transform import transform_data
from scripts.load_to_sql import load_to_sql

# Load environment variables
load_dotenv()

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DB = os.getenv("SQL_DB")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SQL_SERVER};DATABASE={SQL_DB};"
    f"UID={SQL_USER};PWD={SQL_PASSWORD}"
)

input_path = "data/sample_data_10k.csv"
table_name = "royalties_table"

print("🔄 Starting ETL pipeline...")
df = transform_data(input_path)
load_to_sql(df, table_name, connection_string)
print("✅ ETL pipeline finished successfully.")
