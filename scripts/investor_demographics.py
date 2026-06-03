import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Age Group Count
age_counts = df["age_group"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    age_counts,
    labels=age_counts.index,
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.savefig(
    "reports/age_group_distribution.png"
)

plt.show()

sip_df = df[df["transaction_type"] == "SIP"]

plt.figure(figsize=(8,5))

sns.boxplot(
    data=sip_df,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount Distribution by Age Group")

plt.savefig(
    "reports/sip_by_age_group.png"
)

plt.show()

print("Demographic Charts Saved Successfully")