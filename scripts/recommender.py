"""
Mutual Fund Recommendation Engine

Generates mutual fund recommendations
based on investor risk appetite using
historical returns, Sharpe ratio, and
expense ratio metrics.

Risk Categories:
- Low Risk
- Moderate Risk
- High Risk

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""



import pandas as pd

df = pd.read_csv("data/processed/clean_performance.csv")

def recommend_funds(risk_appetite):
    risk_map = {
        "Low": ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High"]
    }

    selected_risks = risk_map.get(risk_appetite, ["Moderate"])

    filtered = df[df["risk_grade"].isin(selected_risks)]

    recommendations = (
        filtered.sort_values("sharpe_ratio", ascending=False)
        .head(3)
        [
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "return_3yr_pct",
                "sharpe_ratio",
                "expense_ratio_pct"
            ]
        ]
    )

    return recommendations

for risk in ["Low", "Moderate", "High"]:
    print(f"\n===== Recommendations for {risk} Risk Investor =====")
    print(recommend_funds(risk))