import pandas as pd

def transform_data(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and applies basic transformations.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    df = pd.read_csv(file_path)

    # Convert month and release date to datetime
    df['month'] = pd.to_datetime(df['month'], format='%Y-%m')
    df['track_release_date'] = pd.to_datetime(df['track_release_date'])

    # Rename columns to snake_case
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Fill NAs if needed
    df['royalties_usd'] = df['royalties_usd'].fillna(0)

    # Remove duplicates
    df = df.drop_duplicates()

    return df

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("❌ Usage: python transform.py <input_csv_path>")
    else:
        input_path = sys.argv[1]
        df = transform_data(input_path)
        print("✅ Data transformed successfully.")
        print(df.head())
