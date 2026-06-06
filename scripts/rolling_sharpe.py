import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load returns
df = pd.read_csv("data/processed/returns_computed.csv")

# Select first 5 funds
funds = df["amfi_code"].unique()[:5]

plt.figure(figsize=(12,6))

for fund in funds:

    temp = df[df["amfi_code"] == fund].copy()

    rolling_sharpe = (
        temp["daily_return"].rolling(90).mean()
        /
        temp["daily_return"].rolling(90).std()
    ) * np.sqrt(252)

    plt.plot(
        temp["date"],
        rolling_sharpe,
        label=str(fund)
    )

plt.title("Rolling 90-Day Sharpe Ratio")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/rolling_sharpe_chart.png"
)

print("Rolling Sharpe Chart Saved Successfully")