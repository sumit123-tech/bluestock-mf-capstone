import pandas as pd
import matplotlib.pyplot as plt

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

latest = aum[aum["date"] == aum["date"].max()]

latest = latest.sort_values(
    "aum_crore",
    ascending=False
)

plt.figure(figsize=(10,5))

plt.bar(
    latest["fund_house"],
    latest["aum_crore"]
)

plt.xticks(rotation=45)

plt.title("Top Fund Houses by AUM")
plt.ylabel("AUM (Crore)")

plt.tight_layout()

plt.savefig("reports/aum_chart.png")

print("Chart saved in reports folder")