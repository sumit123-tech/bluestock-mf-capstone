# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique fund identifier |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Fund scheme name |
| category | Text | Fund category |
| risk_category | Text | Risk classification |

---

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

...