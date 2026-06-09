"""
Alpha and Beta Analysis

Calculates fund Alpha and Beta against benchmark returns
to measure benchmark outperformance and market sensitivity.

Output:
- reports/alpha_beta.csv

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""



import pandas as pd
import numpy as np

# Fund returns
returns = pd.read_csv("data/processed/returns_computed.csv")

# Benchmark
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

benchmark = benchmark[benchmark["index_name"] == "NIFTY50"]

benchmark["date"] = pd.to_datetime(benchmark["date"])
benchmark = benchmark.sort_values("date")

benchmark["benchmark_return"] = benchmark["close_value"].pct_change()

benchmark = benchmark.dropna()

results = []

for amfi_code, fund in returns.groupby("amfi_code"):

    fund["date"] = pd.to_datetime(fund["date"])

    merged = pd.merge(
        fund,
        benchmark[["date", "benchmark_return"]],
        on="date",
        how="inner"
    )

    if len(merged) < 30:
        continue

    x = merged["benchmark_return"]
    y = merged["daily_return"]

    beta = np.cov(y, x)[0, 1] / np.var(x)

    alpha = (
        y.mean() - beta * x.mean()
    ) * 252

    results.append({
        "amfi_code": amfi_code,
        "alpha": round(alpha, 4),
        "beta": round(beta, 4)
    })

alpha_beta_df = pd.DataFrame(results)

alpha_beta_df.to_csv(
    "reports/alpha_beta.csv",
    index=False
)

print("Alpha Beta Calculation Completed")