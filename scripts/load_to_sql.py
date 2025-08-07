import pandas as pd
import pyodbc

def load_to_sql(df: pd.DataFrame, table_name: str, connection_string: str):
    """
    Loads a DataFrame into a SQL Server table.

    Args:
        df (pd.DataFrame): Transformed DataFrame.
        table_name (str): Destination table name.
        connection_string (str): ODBC connection string.
    """
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Optional: create table if it doesn't exist
    create_table_query = f"""
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}')
    BEGIN
        CREATE TABLE {table_name} (
            artist_id VARCHAR(10),
            artist_name VARCHAR(255),
            month DATE,
            royalties_usd FLOAT,
            spotify_streams INT,
            instagram_followers INT,
            twitter_followers INT,
            track_release_date DATE
        )
    END
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data row by row
    for index, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (
                artist_id, artist_name, month, royalties_usd,
                spotify_streams, instagram_followers,
                twitter_followers, track_release_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Loaded {len(df)} rows into '{table_name}'.")

if __name__ == "__main__":
    from transform import transform_data
    import sys

    if len(sys.argv) != 4:
        print("❌ Usage: python load_to_sql.py <input_csv_path> <table_name> <connection_string>")
    else:
        csv_path = sys.argv[1]
        table = sys.argv[2]
        conn_str = sys.argv[3]

        df = transform_data(csv_path)
        load_to_sql(df, table, conn_str)
