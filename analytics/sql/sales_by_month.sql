SELECT
    year,
    month,
    SUM(sales_amount) AS total_sales
FROM fact_sales fs
JOIN dim_date dd ON fs.date_id = dd.date_id
GROUP BY year, month
ORDER BY year, month;