import pandas as pd
import matplotlib.pyplot as plt

# Load data
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

# Convert month column
sip["month"] = pd.to_datetime(sip["month"])

# Plot
plt.figure(figsize=(12,6))
plt.plot(sip["month"], sip["sip_inflow_crore"])

# Mark highest SIP inflow
max_row = sip.loc[sip["sip_inflow_crore"].idxmax()]

plt.scatter(
    max_row["month"],
    max_row["sip_inflow_crore"]
)

plt.annotate(
    f"{max_row['sip_inflow_crore']} Cr",
    (max_row["month"], max_row["sip_inflow_crore"])
)

plt.title("Monthly SIP Inflow Trend")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore)")
plt.grid(True)

plt.tight_layout()

plt.savefig("reports/sip_inflow_trend.png")

print("Chart Saved Successfully")
print("Maximum SIP Inflow:", max_row["sip_inflow_crore"])