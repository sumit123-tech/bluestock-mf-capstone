import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = master_codes - nav_codes

print("\n===== AMFI CODE VALIDATION =====")
print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))

print("\nMissing Codes:")
print(missing_codes)

if len(missing_codes) == 0:
    print("\nSUCCESS: All AMFI codes from fund_master exist in nav_history.")
else:
    print("\nWARNING: Some codes are missing.")