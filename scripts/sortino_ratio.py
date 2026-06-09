"""
Sortino Ratio Analysis

Calculates downside risk-adjusted return for each fund
using negative return volatility.

Output:
- reports/sortino_values.csv

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""

import pandas as pd
import numpy as np

returns = pd.read_csv("data/processed/returns_computed.csv")

risk_free_rate = 0.065

results = []

for amfi_code, group in returns.groupby("amfi_code"):

    annual_return = group["daily_return"].mean() * 252

    downside_returns = group[group["daily_return"] < 0]["daily_return"]

    downside_std = downside_returns.std() * np.sqrt(252)

    if downside_std == 0 or np.isnan(downside_std):
        sortino = np.nan
    else:
        sortino = (annual_return - risk_free_rate) / downside_std

    results.append({
        "amfi_code": amfi_code,
        "sortino_ratio": round(sortino, 3)
        if pd.notnull(sortino)
        else np.nan
    })

sortino_df = pd.DataFrame(results)

sortino_df.to_csv(
    "reports/sortino_values.csv",
    index=False
)

print("Sortino Ratios Calculated Successfully")
print(sortino_df.head())