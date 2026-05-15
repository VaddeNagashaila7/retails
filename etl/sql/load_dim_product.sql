







-- Step 1: Load into staging table
COPY staging_product(product_name, category, subcategory, unit_price)
FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/products.csv'
DELIMITER ',' CSV HEADER;

-- Step 2: Insert unique records into dimension
INSERT INTO dim_product (product_name, category, subcategory, unit_price)
SELECT DISTINCT product_name, category, subcategory, unit_price
FROM staging_product
ON CONFLICT (product_name, category, subcategory, unit_price)
DO NOTHING;
-- 




-- -- COPY dim_product(product_name, category, subcategory, unit_price)
-- -- FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/products.csv'
-- -- -- DELIMITER ',' CSV HEADER;