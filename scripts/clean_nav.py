import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# date to datetime
df["date"] = pd.to_datetime(df["date"])

# sort
df = df.sort_values(["amfi_code", "date"])

# remove duplicates
df = df.drop_duplicates()

# forward fill nav by fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# validate nav > 0
df = df[df["nav"] > 0]

# save
df.to_csv("data/processed/clean_nav.csv", index=False)

print(df.shape)
print("Clean NAV saved")