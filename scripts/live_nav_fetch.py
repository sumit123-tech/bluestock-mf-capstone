import requests
import pandas as pd
from pathlib import Path

# Create output folder
output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

schemes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching {name} ({code})...")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = output_folder / f"{name}_nav.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    else:
        print(f"Failed for {code}")