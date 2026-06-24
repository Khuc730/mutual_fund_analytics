import pandas as pd
import os 

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print(f"\nTotal CSV Files found : {len(csv_files)}")

for file in csv_files:
    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    file_path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate rows")
    print(df.duplicated().sum())