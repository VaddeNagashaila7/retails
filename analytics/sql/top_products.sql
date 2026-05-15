SELECT
    p.product_name,
    SUM(fs.sales_amount) AS revenue
FROM fact_sales fs
JOIN dim_product p ON fs.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;