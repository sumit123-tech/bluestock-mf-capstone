import pandas as pd
import matplotlib.pyplot as plt

# Load NAV data
nav = pd.read_csv("data/processed/clean_nav.csv")

# Load benchmark
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Top 5 funds from scorecard
top_funds = [120505, 148567, 120843, 100033, 148569]

plt.figure(figsize=(12,6))

for fund in top_funds:
    temp = nav[nav["amfi_code"] == fund]

    if len(temp) > 0:
        base = temp["nav"].iloc[0]

        plt.plot(
            temp["date"],
            (temp["nav"]/base)*100,
            label=str(fund)
        )

# NIFTY50 Benchmark
nifty = benchmark[benchmark["index_name"]=="NIFTY50"]

base_nifty = nifty["close_value"].iloc[0]

plt.plot(
    nifty["date"],
    (nifty["close_value"]/base_nifty)*100,
    linewidth=3,
    label="NIFTY50"
)

plt.title("Top Funds vs NIFTY50")
plt.xlabel("Date")
plt.ylabel("Growth Index")
plt.legend()

plt.tight_layout()

plt.savefig("reports/benchmark_chart.png")

print("Benchmark Chart Saved Successfully")