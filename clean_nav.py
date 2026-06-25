import pandas as pd 

df = pd.read_csv("data/raw/02_nav_history.csv")

print("\nColumns:",df.columns)

print("\nFirst 5 rows:",df.head())

print("\nData Types: ",df.dtypes)

print("\n Shape: ",df.shape)

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    by=["amfi_code","date"]
)

print("\nMissing NAV values: ",df["nav"].isnull().sum())


df["nav"] = df.groupby(                 
    "amfi_code"
)["nav"].ffill()                #forward fill NAV within each fund 

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("\nDuplicates Removed:", before - after)

invalid_nav = df[df["nav"] <= 0]

print("\nNumber of Invalid NAV Records : ",len(invalid_nav))

df.to_csv("data/processed/clean_nav.csv",
          index = False
)

print("\nClean file saved!")
print("Final Shape:", df.shape)