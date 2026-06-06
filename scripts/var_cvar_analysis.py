import pandas as pd
import numpy as np

# Load daily returns
returns = pd.read_csv("data/processed/returns_computed.csv")

results = []

for amfi_code, group in returns.groupby("amfi_code"):

    daily_returns = group["daily_return"].dropna()

    # Historical VaR at 95% confidence = 5th percentile
    var_95 = np.percentile(daily_returns, 5)

    # CVaR = average loss beyond VaR
    cvar_95 = daily_returns[daily_returns <= var_95].mean()

    results.append({
        "amfi_code": amfi_code,
        "var_95_pct": round(var_95 * 100, 2),
        "cvar_95_pct": round(cvar_95 * 100, 2)
    })

var_df = pd.DataFrame(results)

var_df.to_csv(
    "reports/var_cvar_report.csv",
    index=False
)

print("VaR and CVaR Report Created Successfully")
print(var_df.head())