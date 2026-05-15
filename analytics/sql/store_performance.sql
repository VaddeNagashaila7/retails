SELECT
    s.store_name,
    SUM(fs.sales_amount) AS total_sales
FROM fact_sales fs
JOIN dim_store s ON fs.store_id = s.store_id
GROUP BY s.store_name;