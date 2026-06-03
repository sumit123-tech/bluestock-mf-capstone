import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

sip_df = df[df["transaction_type"] == "SIP"]

state_sip = (
    sip_df.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

state_sip.plot(kind="barh")

plt.title("Total SIP Amount by State")
plt.xlabel("Amount (INR)")
plt.ylabel("State")

plt.tight_layout()

plt.savefig(
    "reports/state_sip_distribution.png"
)

plt.show()

city_tier = df["city_tier"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    city_tier,
    labels=city_tier.index,
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 Investors")

plt.savefig(
    "reports/t30_b30_distribution.png"
)

plt.show()

print("Geographic Charts Saved Successfully")