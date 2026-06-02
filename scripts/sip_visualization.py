import pandas as pd
import matplotlib.pyplot as plt

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

sip["month"] = pd.to_datetime(sip["month"])

plt.figure(figsize=(10,5))
plt.plot(sip["month"], sip["sip_inflow_crore"])

plt.title("Monthly SIP Inflows")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore)")
plt.grid(True)

plt.tight_layout()

plt.savefig("reports/sip_trend.png")

print("Chart saved in reports folder")
