import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

for file in sorted(data_path.glob("*.csv")):
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print(f"\nShape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())