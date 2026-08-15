-- ==========================================
-- CHURNGUARD AI
-- ADVANCED CHURN ANALYSIS
-- ==========================================


-- 1. High-Risk Contract + Internet Segment

SELECT
    Contract,
    InternetService,

    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY
    Contract,
    InternetService

ORDER BY churn_rate DESC;


-- 2. Contract + Payment Method

SELECT
    Contract,
    PaymentMethod,

    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY
    Contract,
    PaymentMethod

ORDER BY churn_rate DESC;


-- 3. Contract + Internet + Payment

SELECT
    Contract,
    InternetService,
    PaymentMethod,

    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY
    Contract,
    InternetService,
    PaymentMethod

HAVING COUNT(*) >= 50

ORDER BY churn_rate DESC;


-- 4. New Customers with Month-to-Month Contract

SELECT
    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

WHERE
    tenure <= 12
    AND Contract = 'Month-to-month';


-- 5. High Monthly Charge Customers

SELECT
    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

WHERE MonthlyCharges > 70;


-- 6. Customers Without Tech Support

SELECT
    TechSupport,

    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY TechSupport

ORDER BY churn_rate DESC;


-- 7. Customers Without Online Security

SELECT
    OnlineSecurity,

    COUNT(*) AS total_customers,

    SUM(Churn) AS churned_customers,

    ROUND(
        100.0 * SUM(Churn) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY OnlineSecurity

ORDER BY churn_rate DESC;