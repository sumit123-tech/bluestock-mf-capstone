import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")
performance = pd.read_csv("data/processed/clean_performance.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

# Check dtypes
print("\nTransactions Dtypes:")
print(transactions.dtypes)

# Select required columns for dim_fund
dim_fund = fund_master[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "benchmark",
        "risk_category"
    ]
]

# Rename nav date column
nav = nav.rename(columns={"date": "nav_date"})

print("Loading dim_fund...")
dim_fund.to_sql("dim_fund", engine, if_exists="replace", index=False)

print("Loading fact_nav...")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

print("Loading fact_transactions...")
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

print("Loading fact_performance...")
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Loading fact_sip...")
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)

print("Database Created Successfully")