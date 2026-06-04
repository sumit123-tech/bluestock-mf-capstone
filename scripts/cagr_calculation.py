import pandas as pd

# Load NAV data
nav = pd.read_csv("data/processed/clean_nav.csv")

nav["date"] = pd.to_datetime(nav["date"])

results = []

for amfi_code, group in nav.groupby("amfi_code"):

    group = group.sort_values("date")

    start_nav = group.iloc[0]["nav"]
    end_nav = group.iloc[-1]["nav"]

    years = (
        (group.iloc[-1]["date"] - group.iloc[0]["date"]).days
        / 365.25
    )

    cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    results.append(
        {
            "amfi_code": amfi_code,
            "start_nav": round(start_nav, 2),
            "end_nav": round(end_nav, 2),
            "years": round(years, 2),
            "cagr_pct": round(cagr, 2)
        }
    )

cagr_df = pd.DataFrame(results)

cagr_df.to_csv(
    "reports/cagr_report.csv",
    index=False
)

print("CAGR Report Created Successfully")
print(cagr_df.head())