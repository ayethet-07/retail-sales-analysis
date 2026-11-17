-- Retail Sales Analysis — SQLite
-- Table name: retail_sales
-- Import retail_sales.csv with headers enabled. Keep spaces in column names as shown.

-- 1) Which category generates the most sales?
SELECT
    "Product Category" AS category,
    SUM("Total Amount") AS total_sales,
    ROUND(100.0 * SUM("Total Amount") /
          (SELECT SUM("Total Amount") FROM retail_sales), 1) AS sales_share_pct,
    COUNT(*) AS transactions
FROM retail_sales
GROUP BY "Product Category"
ORDER BY total_sales DESC;

-- 2) What are monthly sales and month-over-month growth?
-- The 2024-01 value is a partial month (only two transactions in the source).
WITH monthly AS (
    SELECT
        strftime('%Y-%m', date("Date")) AS sales_month,
        SUM("Total Amount") AS monthly_sales
    FROM retail_sales
    GROUP BY strftime('%Y-%m', date("Date"))
),
with_previous AS (
    SELECT
        sales_month,
        monthly_sales,
        LAG(monthly_sales) OVER (ORDER BY sales_month) AS previous_month_sales
    FROM monthly
)
SELECT
    sales_month,
    monthly_sales,
    ROUND(100.0 * (monthly_sales - previous_month_sales) /
          NULLIF(previous_month_sales, 0), 1) AS mom_growth_pct
FROM with_previous
ORDER BY sales_month;

-- 3) What is the average transaction value and average number of units per basket?
SELECT
    COUNT(*) AS transactions,
    SUM("Total Amount") AS total_sales,
    ROUND(AVG("Total Amount"), 2) AS average_transaction_value,
    SUM("Quantity") AS units_sold,
    ROUND(AVG("Quantity"), 2) AS average_units_per_transaction
FROM retail_sales;

-- 4) Which categories perform best by gender?
SELECT
    "Gender" AS gender,
    "Product Category" AS category,
    COUNT(*) AS transactions,
    SUM("Quantity") AS units_sold,
    SUM("Total Amount") AS total_sales
FROM retail_sales
GROUP BY "Gender", "Product Category"
ORDER BY gender, total_sales DESC;

-- 5) Which dates generated the highest sales?
SELECT
    date("Date") AS sales_date,
    COUNT(*) AS transactions,
    SUM("Total Amount") AS daily_sales
FROM retail_sales
GROUP BY date("Date")
ORDER BY daily_sales DESC
LIMIT 10;
