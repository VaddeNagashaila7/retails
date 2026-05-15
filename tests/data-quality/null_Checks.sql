SELECT *
FROM fact_sales
WHERE
    date_id IS NULL
 OR customer_id IS NULL
 OR product_id IS NULL
 OR store_id IS NULL;