import pandas as pd

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\n===== TOP 10 FUNDS BY 5 YEAR RETURN =====")

top10 = (
    perf.sort_values("return_5yr_pct", ascending=False)
        [["scheme_name", "fund_house", "return_5yr_pct"]]
        .head(10)
)

print(top10)