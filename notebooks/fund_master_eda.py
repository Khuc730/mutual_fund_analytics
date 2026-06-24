import pandas as pd 

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique fund houses : ")
print(df["fund_house"].unique())

print("\nTotal fund houses : ")
print(df["fund_house"].nunique())

print("\nCategories : ")
print(df["category"].unique())

print("\nTotal Categories : ")
print(df["category"].nunique())

print("\nSub Category : ")
print(df["risk_category"].unique())

print("\nTotal Risk Categories : ")
print(df["risk_category"].nunique())
