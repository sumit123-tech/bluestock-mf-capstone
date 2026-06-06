import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df["weight_decimal"] = df["weight_pct"] / 100

hhi = (
    df.groupby("amfi_code")
    .apply(lambda x: (x["weight_decimal"] ** 2).sum())
    .reset_index(name="sector_hhi")
)

hhi.to_csv("reports/sector_hhi.csv", index=False)

print("Sector HHI Analysis Completed")
print(hhi.head())