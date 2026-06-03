import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/05_category_inflows.csv")

pivot_table = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

plt.figure(figsize=(14,6))

sns.heatmap(
    pivot_table,
    cmap="YlGnBu",
    annot=False
)

plt.title("Category-wise Net Inflows Heatmap")
plt.xlabel("Month")
plt.ylabel("Category")

plt.tight_layout()

plt.savefig(
    "reports/category_heatmap.png"
)

plt.show()

print("Heatmap Saved Successfully")