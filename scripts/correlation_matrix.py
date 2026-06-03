import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load NAV data
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Pivot table
nav_pivot = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = nav_pivot.pct_change().dropna()

# Correlation matrix
corr_matrix = returns.corr()

plt.figure(figsize=(12, 8))

sns.heatmap(
    corr_matrix,
    cmap="coolwarm",
    center=0
)

plt.title("Fund Return Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "reports/correlation_matrix.png"
)

plt.show()

print("Correlation Matrix Saved Successfully")