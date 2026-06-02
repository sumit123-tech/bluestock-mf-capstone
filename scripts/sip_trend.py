import pandas as pd

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("\n===== SIP INFLOW SUMMARY =====")

print("Average SIP Inflow:", sip["sip_inflow_crore"].mean())
print("Maximum SIP Inflow:", sip["sip_inflow_crore"].max())
print("Minimum SIP Inflow:", sip["sip_inflow_crore"].min())