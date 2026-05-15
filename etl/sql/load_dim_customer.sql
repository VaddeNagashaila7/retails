-- Step 1: Load into staging
COPY staging_customer(customer_name, gender, city, state, country)
FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/customers.csv'
DELIMITER ',' CSV HEADER;

-- Step 2: Insert without duplicates
INSERT INTO dim_customer (customer_name, gender, city, state, country)
SELECT DISTINCT customer_name, gender, city, state, country
FROM staging_customer
ON CONFLICT (customer_name, gender, city, state, country)
DO NOTHING;






























-- COPY staging_customer(customer_name, gender, city, state, country)
-- FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/customers.csv'
-- DELIMITER ',' CSV HEADER;