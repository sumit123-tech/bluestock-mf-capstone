import pandas as pd
import matplotlib.pyplot as plt

# Load data
nav = pd.read_csv("data/processed/clean_nav.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Select first 5 funds
funds = nav["amfi_code"].unique()[:5]

plt.figure(figsize=(12, 6))

for fund in funds:
    fund_data = nav[nav["amfi_code"] == fund]
    plt.plot(
        fund_data["date"],
        fund_data["nav"],
        label=str(fund)
    )

plt.title("NAV Trend Analysis (Sample Funds)")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("reports/nav_trend.png")

print("Chart saved: reports/nav_trend.png")