SELECT
    c.customer_name,
    SUM(fs.sales_amount) AS lifetime_value
FROM fact_sales fs
JOIN dim_customer c
  ON fs.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY lifetime_value DESC;