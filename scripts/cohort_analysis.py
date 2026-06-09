"""
Investor Cohort Analysis

Groups investors by their first transaction year
to analyze investment behavior, investor count,
and total investment contribution by cohort.

Output:
- reports/cohort_analysis.csv

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""



import pandas as pd

# Load transactions
df = pd.read_csv("data/processed/clean_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# First transaction per investor
first_txn = (
    df.groupby("investor_id")["transaction_date"]
    .min()
    .reset_index()
)

first_txn["cohort_year"] = first_txn["transaction_date"].dt.year

# Merge back
df = df.merge(
    first_txn[["investor_id", "cohort_year"]],
    on="investor_id",
    how="left"
)

# Cohort summary
cohort = (
    df.groupby("cohort_year")
    .agg(
        total_investment=("amount_inr", "sum"),
        avg_investment=("amount_inr", "mean"),
        investor_count=("investor_id", "nunique")
    )
    .reset_index()
)

cohort.to_csv(
    "reports/cohort_analysis.csv",
    index=False
)

print("Cohort Analysis Completed")
