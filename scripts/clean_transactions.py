import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# validate amount > 0
df = df[df["amount_inr"] > 0]

# standardize date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# check kyc values
print("\n===== KYC STATUS =====")
print(df["kyc_status"].unique())

# remove duplicates
df = df.drop_duplicates()

# save
df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("\nShape:", df.shape)
print("Clean Transactions Saved")