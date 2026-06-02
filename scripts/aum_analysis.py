import pandas as pd

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

latest_date = aum["date"].max()

latest = aum[aum["date"] == latest_date]

print("\n===== TOP FUND HOUSES BY AUM =====")

print(
    latest.sort_values("aum_crore", ascending=False)
          [["fund_house", "aum_crore"]]
          .head(10)
)