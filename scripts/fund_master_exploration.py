import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

# Unique Fund Houses
print("\n===== FUND HOUSES =====")
print(df["fund_house"].unique())

# Unique Categories
print("\n===== CATEGORIES =====")
print(df["category"].unique())

# Unique Sub Categories
print("\n===== SUB CATEGORIES =====")
print(df["sub_category"].unique())

# Unique Risk Categories
print("\n===== RISK CATEGORIES =====")
print(df["risk_category"].unique())