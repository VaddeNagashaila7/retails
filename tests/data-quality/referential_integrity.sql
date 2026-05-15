SELECT *
FROM fact_sales fs
LEFT JOIN dim_customer dc
  ON fs.customer_id = dc.customer_id
WHERE dc.customer_id IS NULL;