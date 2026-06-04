import pandas as pd

# Load cleaned NAV data
nav = pd.read_csv("data/processed/clean_nav.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# Calculate daily returns
nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

# Remove first null return for each fund
nav = nav.dropna(subset=["daily_return"])

# Save
nav.to_csv(
    "data/processed/returns_computed.csv",
    index=False
)

print("Returns Computed Successfully")
print("Shape:", nav.shape)

print("\nSample:")
print(nav.head())