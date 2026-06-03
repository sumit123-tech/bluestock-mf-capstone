-- 1. Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV

SELECT AVG(nav) AS avg_nav
FROM fact_nav;


-- 3. Monthly Average NAV

SELECT substr(nav_date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;


-- 4. Total Transactions by State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio < 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
WHERE expense_ratio_pct < 1;


-- 6. Average SIP Inflow

SELECT AVG(sip_inflow_crore)
FROM fact_sip;


-- 7. Highest 3-Year Return

SELECT scheme_name,
return_3yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY return_3yr_pct DESC
LIMIT 5;


-- 8. Count Funds by Category

SELECT category,
COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;


-- 9. Average Transaction Amount

SELECT AVG(amount_inr)
FROM fact_transactions;


-- 10. Morningstar Rating Distribution

SELECT morningstar_rating,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY morningstar_rating
ORDER BY morningstar_rating;