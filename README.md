#  Mutual Fund Analytics Capstone Project

##  Project Overview

The Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, SIP trends, portfolio risk, and market insights.

The project integrates multiple mutual fund datasets, performs ETL processing using Python, stores cleaned data in SQLite, generates advanced financial analytics, and visualizes insights through an interactive Power BI dashboard.

---

##  Project Objectives

* Consolidate multiple mutual fund datasets into a unified analytics platform.
* Analyze fund performance using risk-adjusted metrics.
* Track SIP inflows and investor participation trends.
* Evaluate portfolio concentration and downside risk.
* Build interactive Power BI dashboards for business insights.
* Generate data-driven fund recommendations based on investor risk profiles.

---

##  Data Sources

The project uses 10+ datasets along with live MFAPI integration.

### Core Datasets

* Fund Master Data
* NAV History
* AUM Data
* SIP Inflows
* Investor Transactions
* Portfolio Holdings
* Benchmark Data
* Category Inflows
* Industry Folios
* Fund Performance Metrics

### External Source

* MFAPI (Live Mutual Fund NAV Data)

---

##  Technology Stack

| Tool | Purpose |
|------|----------|
| Python | ETL & Analytics |
| Pandas | Data Processing |
| NumPy | Numerical Analysis |
| SciPy | Statistical Analytics |
| SQLite | Data Storage |
| SQLAlchemy | Database Integration |
| Power BI | Dashboard Development |
| GitHub | Version Control |


##  Project Architecture

```text
Raw CSV Files & APIs
        ↓
Python ETL & Data Cleaning
        ↓
SQLite Database
        ↓
Analytics Engine
        ↓
Power BI Dashboard
        ↓
Business Insights
```

##  Exploratory Data Analysis (EDA)

Key analyses performed:

* NAV Trend Analysis
* SIP Inflow Trend Analysis
* AUM Growth Analysis
* Investor Demographic Analysis
* State-wise Investment Analysis
* Correlation Matrix Analysis

### Key Insights

* NAV values showed consistent growth across major equity-oriented funds.
* SIP inflows increased steadily throughout the analysis period.
* Industry AUM demonstrated strong long-term growth.
* Investor activity was concentrated across key age groups and major states.

---

##  Performance Analytics

The following financial metrics were calculated:

* CAGR (Compound Annual Growth Rate)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard Ranking

### Project Highlights

* Highest Sharpe Ratio: 1.09
* Highest Sortino Ratio: 1.83
* Best Fund Score: 100
* Lowest Drawdown: -4.31%

---

##  Advanced Analytics & Modeling

### 1. VaR & CVaR Analysis

Calculated Value at Risk (VaR) and Conditional Value at Risk (CVaR) to measure downside risk exposure.

### 2. Rolling Sharpe Ratio

Tracked risk-adjusted performance consistency over time.

### 3. Cohort Analysis

Analyzed investor retention and investment growth by onboarding period.

### 4. SIP Continuity Analysis

Identified investors at risk of SIP discontinuation using transaction frequency and average gap analysis.

### 5. Sector HHI Analysis

Measured portfolio concentration and diversification risk using the Herfindahl-Hirschman Index.

### 6. Recommendation Engine

Generated mutual fund recommendations based on investor risk profiles.

---

##  Power BI Dashboard Pages

### Page 1: Industry Overview

* Total AUM
* Total SIP Inflow
* Total Folios
* Total Schemes
* Top Fund Houses
* Industry AUM Trend

### Page 2: Fund Performance

* Fund Scorecard
* NAV Trends
* Risk vs Return Analysis
* Fund Comparison

### Page 3: Investor Analytics

* Age Group Analysis
* State-wise Investments
* Transaction Distribution
* Monthly Transaction Volume

### Page 4: SIP & Market Trends

* SIP Inflow Trends
* Category Inflow Analysis
* Market Insights

---

##  Project Structure

```text
bluestock-mf-capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
├── reports/
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── presentation/
│   └── Mutual_Fund_Analytics_Presentation.pptx
│
├── README.md
├── requirements.txt
└── .gitignore
```

##  How to Run

1. Clone the repository

```bash
git clone https://github.com/sumit123-tech/bluestock-mf-capstone.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run analytics scripts

```bash
python scripts/var_cvar_analysis.py
python scripts/rolling_sharpe.py
python scripts/cohort_analysis.py
python scripts/sip_continuity.py
python scripts/recommender.py
python scripts/sector_hhi.py
```

4. Open Power BI Dashboard

```text
dashboard/bluestock_mf_dashboard.pbix
```

---

##  Key Business Recommendations

### Low Risk Investors

* Liquid Funds
* Ultra Short Duration Funds

### Moderate Risk Investors

* Large Cap Funds
* Balanced Advantage Funds

### High Risk Investors

* Mid Cap Funds
* Small Cap Funds
* Sectoral Funds

---

##  Author

**Sumit Banerjee**
Data Analyst Intern
Bluestock Fintech

📧 Email: [sumit77185@gmail.com](mailto:sumit77185@gmail.com)

🔗 GitHub: https://github.com/sumit123-tech

---

##  Project Outcome

Successfully developed an end-to-end Mutual Fund Analytics platform integrating ETL, SQL, advanced financial analytics, and Power BI dashboards to generate actionable investment insights.
