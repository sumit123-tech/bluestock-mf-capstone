import pandas as pd

nav = pd.read_csv("data/processed/clean_nav.csv")

nav["date"] = pd.to_datetime(nav["date"])

results = []

for amfi_code, group in nav.groupby("amfi_code"):

    group = group.sort_values("date")

    running_max = group["nav"].cummax()

    drawdown = (group["nav"] / running_max) - 1

    max_dd = drawdown.min()

    results.append({
        "amfi_code": amfi_code,
        "max_drawdown_pct": round(max_dd * 100, 2)
    })

max_dd_df = pd.DataFrame(results)

max_dd_df.to_csv(
    "reports/max_drawdown.csv",
    index=False
)

print("Maximum Drawdown Calculated Successfully")
print(max_dd_df.head())