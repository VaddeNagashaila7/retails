SELECT
    date_id,
    customer_id,
    product_id,
    store_id,
    COUNT(*) AS duplicates
FROM fact_sales
GROUP BY
    date_id, customer_id, product_id, store_id
HAVING COUNT(*) > 1;