-- ==========================================
-- CHURNGUARD AI
-- CUSTOMER ANALYSIS
-- ==========================================


-- 1. Total Customers
SELECT
    COUNT(*) AS total_customers
FROM customers;


-- 2. Total Churned Customers
SELECT
    SUM(Churn) AS churned_customers
FROM customers;


-- 3. Overall Churn Rate
SELECT
    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate
FROM customers;


-- 4. Churn by Contract
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate
FROM customers
GROUP BY Contract
ORDER BY churn_rate DESC;


-- 5. Churn by Internet Service
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate
FROM customers
GROUP BY InternetService
ORDER BY churn_rate DESC;


-- 6. Churn by Payment Method
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;


-- 7. Churn by Tenure Group
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END AS tenure_group,

    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END

ORDER BY churn_rate DESC;


-- 8. Churn by Senior Citizen
SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY SeniorCitizen

ORDER BY churn_rate DESC;


-- 9. Average Monthly Charges by Churn
SELECT
    Churn,
    ROUND(
        AVG(MonthlyCharges),
        2
    ) AS avg_monthly_charges

FROM customers

GROUP BY Churn;


-- 10. Average Tenure by Churn
SELECT
    Churn,
    ROUND(
        AVG(tenure),
        2
    ) AS avg_tenure

FROM customers

GROUP BY Churn;