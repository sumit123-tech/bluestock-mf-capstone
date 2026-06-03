import pandas as pd
import matplotlib.pyplot as plt

# Load data
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Convert date
aum["date"] = pd.to_datetime(aum["date"])

# Latest date data
latest_date = aum["date"].max()

latest_aum = aum[aum["date"] == latest_date]

# Sort by AUM
latest_aum = latest_aum.sort_values(
    by="aum_crore",
    ascending=False
)

plt.figure(figsize=(12,6))

plt.bar(
    latest_aum["fund_house"],
    latest_aum["aum_crore"]
)

plt.xticks(rotation=45, ha="right")
plt.title("Top Fund Houses by AUM")
plt.xlabel("Fund House")
plt.ylabel("AUM (Crore)")

plt.tight_layout()

plt.savefig("reports/aum_growth.png")

print("Chart saved: reports/aum_growth.png")
