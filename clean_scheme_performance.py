import pandas as pd 

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Columns : ",df.columns)

print("First 5 Rows : ",df.head())

print("Data Types: ",df.dtypes)

print("Original shape : ",df.shape)

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records : ",
      len(invalid_expense))

negative_sharpe = df[
    df["sharpe_ratio"] < 0
]

print("\nFunds with Negative Sharpe Ratio: ",len(negative_sharpe))

before = len(df)
df = df.drop_duplicates()
after = len(df)
print("\nDuplicates Removed : ",before - after)

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)
print("\nClean file saved successfully!")
print("Final Shape : ",df.shape)