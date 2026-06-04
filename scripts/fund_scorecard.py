import pandas as pd

# Load reports
cagr = pd.read_csv("reports/cagr_report.csv")
sharpe = pd.read_csv("reports/sharpe_values.csv")
alpha_beta = pd.read_csv("reports/alpha_beta.csv")
drawdown = pd.read_csv("reports/max_drawdown.csv")

# Load expense ratio
performance = pd.read_csv("data/processed/clean_performance.csv")

expense = performance[["amfi_code", "expense_ratio_pct"]]

# Merge
df = cagr.merge(sharpe, on="amfi_code")
df = df.merge(alpha_beta, on="amfi_code")
df = df.merge(drawdown, on="amfi_code")
df = df.merge(expense, on="amfi_code")

# Rankings
df["cagr_rank"] = df["cagr_pct"].rank(ascending=False)
df["sharpe_rank"] = df["sharpe_ratio"].rank(ascending=False)
df["alpha_rank"] = df["alpha"].rank(ascending=False)

df["expense_rank"] = df["expense_ratio_pct"].rank(ascending=True)
df["drawdown_rank"] = df["max_drawdown_pct"].rank(ascending=False)

# Composite score
df["fund_score"] = (
    0.30 * df["cagr_rank"] +
    0.25 * df["sharpe_rank"] +
    0.20 * df["alpha_rank"] +
    0.15 * df["expense_rank"] +
    0.10 * df["drawdown_rank"]
)

# Convert to 0-100 scale
df["fund_score"] = (
    (df["fund_score"].max() - df["fund_score"])
    /
    (df["fund_score"].max() - df["fund_score"].min())
) * 100

df = df.sort_values("fund_score", ascending=False)

df.to_csv(
    "reports/fund_scorecard.csv",
    index=False
)

print("Fund Scorecard Created Successfully")
print(df[["amfi_code", "fund_score"]].head(10))