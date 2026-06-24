import requests
import pandas as pd
"""
#HDFC Top 100 Direct Plan Growth
scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        "data/raw/HDFC_Top100_NAV.csv",
        index = False
    )

    print("File has been saved successfully!")
    print(nav_df.head())

else:
    print("API Request has been failed")

"""
funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in funds.items():
    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{fund_name}_NAV.csv",
            index = False
    )

        print(f"{fund_name} has been saved successfully!")

    else:
        print(f"failed to fetch {fund_name}")
