import pandas as pd
import numpy as np

returns = pd.read_csv("data/processed/returns_computed.csv")

risk_free_rate = 0.065

results = []

for amfi_code, group in returns.groupby("amfi_code"):

    mean_return = group["daily_return"].mean() * 252

    std_return = group["daily_return"].std() * np.sqrt(252)

    sharpe = (mean_return - risk_free_rate) / std_return

    results.append(
        {
            "amfi_code": amfi_code,
            "annual_return": round(mean_return * 100, 2),
            "annual_volatility": round(std_return * 100, 2),
            "sharpe_ratio": round(sharpe, 3)
        }
    )

sharpe_df = pd.DataFrame(results)

sharpe_df.to_csv(
    "reports/sharpe_values.csv",
    index=False
)

print("Sharpe Ratios Calculated Successfully")
print(sharpe_df.head())