import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# ensure return columns are numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# negative sharpe ratios
negative_sharpe = df[df["sharpe_ratio"] < 0]

print("\n===== NEGATIVE SHARPE RATIOS =====")
print(negative_sharpe[["scheme_name", "sharpe_ratio"]])

# expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\n===== INVALID EXPENSE RATIOS =====")
print(invalid_expense[["scheme_name", "expense_ratio_pct"]])

# remove duplicates
df = df.drop_duplicates()

# save cleaned file
df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("\nShape:", df.shape)
print("Clean Performance Saved")