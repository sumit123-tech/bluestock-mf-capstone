"""
Sector HHI Analysis

Calculates the Herfindahl-Hirschman Index (HHI)
to measure sector concentration and portfolio
diversification risk across mutual fund schemes.

Output:
- reports/sector_hhi.csv

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""


import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df["weight_decimal"] = df["weight_pct"] / 100

hhi = (
    df.groupby("amfi_code")
    .apply(lambda x: (x["weight_decimal"] ** 2).sum())
    .reset_index(name="sector_hhi")
)

hhi.to_csv("reports/sector_hhi.csv", index=False)

print("Sector HHI Analysis Completed")