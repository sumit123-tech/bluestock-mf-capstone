"""
Master Pipeline Runner

Executes all advanced analytics scripts
for the Mutual Fund Analytics Capstone Project.

Scripts Executed:
- VaR & CVaR Analysis
- Rolling Sharpe Analysis
- Cohort Analysis
- SIP Continuity Analysis
- Recommendation Engine
- Sector HHI Analysis

Author: Sumit Banerjee
Project: Mutual Fund Analytics Capstone
"""

import os

print("Starting Mutual Fund Analytics Pipeline...\n")

scripts = [
    "scripts/var_cvar_analysis.py",
    "scripts/rolling_sharpe.py",
    "scripts/cohort_analysis.py",
    "scripts/sip_continuity.py",
    "scripts/recommender.py",
    "scripts/sector_hhi.py"
]

for script in scripts:
    print(f"Running: {script}")
    os.system(f"python {script}")
    print("-" * 50)

print("\nPipeline Completed Successfully!")