"""
SIP Continuity Analysis

Identifies investors at risk of SIP discontinuation
by analyzing SIP transaction frequency and
average gap between SIP transactions.

Output:
- reports/sip_continuity.csv

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""


import pandas as pd

# Load data
df = pd.read_csv("data/processed/clean_transactions.csv")

# Date conversion
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Only SIP
df["transaction_type"] = df["transaction_type"].str.strip().str.upper()
sip = df[df["transaction_type"] == "SIP"].copy()

results = []

for investor, group in sip.groupby("investor_id"):

    group = group.sort_values("transaction_date")

    if len(group) >= 6:

        gaps = (
            group["transaction_date"]
            .diff()
            .dt.days
            .dropna()
        )

        avg_gap = gaps.mean()

        risk_flag = (
            "At Risk"
            if avg_gap > 35
            else "Active"
        )

        results.append({
            "investor_id": investor,
            "sip_count": len(group),
            "avg_gap_days": round(avg_gap, 2),
            "status": risk_flag
        })

result_df = pd.DataFrame(results)

result_df.to_csv(
    "reports/sip_continuity.csv",
    index=False
)

print("SIP Continuity Analysis Completed")