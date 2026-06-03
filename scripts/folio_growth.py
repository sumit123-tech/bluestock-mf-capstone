import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

plt.figure(figsize=(10,5))

plt.plot(
    df["month"],
    df["total_folios_crore"],
    marker="o"
)

plt.title("Industry Folio Growth")
plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/folio_growth.png"
)

plt.show()

print("Folio Growth Chart Saved Successfully")

print(
    "Growth from",
    df["total_folios_crore"].min(),
    "to",
    df["total_folios_crore"].max(),
    "Crore"
)