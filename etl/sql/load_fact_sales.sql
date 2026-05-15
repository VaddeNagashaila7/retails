-- Step 1: Load into staging
COPY staging_sales(date_id, customer_id, product_id, store_id, quantity, sales_amount)
FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/sales.csv'
DELIMITER ',' CSV HEADER;

-- Step 2: Insert distinct data
INSERT INTO fact_sales (date_id, customer_id, product_id, store_id, quantity, sales_amount)
SELECT DISTINCT date_id, customer_id, product_id, store_id, quantity, sales_amount
FROM staging_sales
ON CONFLICT (date_id, customer_id, product_id, store_id)
DO NOTHING;












-- COPY fact_sales(date_id, customer_id, product_id, store_id, quantity, sales_amount)
-- FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/sales.csv'
-- DELIMITER ',' CSV HEADER;