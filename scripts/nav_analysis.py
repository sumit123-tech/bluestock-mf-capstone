import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

print("\n===== NAV DATA INFO =====")
print(nav.info())

print("\n===== DATE RANGE =====")
print("Start:", nav["date"].min())
print("End:", nav["date"].max())

print("\n===== UNIQUE FUNDS =====")
print(nav["amfi_code"].nunique())