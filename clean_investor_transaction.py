import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Columns: ",df.columns)

print("\nData Types: ",df.dtypes)

print("\nFirst 5 rows: ",df.head())

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

print("\nUnique Transaction Types: ",df["transaction_type"].unique())

invalid_amounts = df[df["amount_inr"] <= 0]

print("\nInvalid Amount Records: ", len(invalid_amounts))

print("\nKYC Status Values: ")
print(df["kyc_status"].unique())

before = len(df)
df = df.drop_duplicates()
after = len(df)

print("\nDuplicates Removed : ", before - after)

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("\nClean file saved successfully!")
print("Final shape : ",df.shape)
