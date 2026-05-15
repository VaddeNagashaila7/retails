-- Step 1: Load into staging
COPY staging_store(store_name, city, state, country)
FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/stores.csv'
DELIMITER ',' CSV HEADER;

-- Step 2: Insert unique records
INSERT INTO dim_store (store_name, city, state, country)
SELECT DISTINCT store_name, city, state, country
FROM staging_store
ON CONFLICT (store_name, city, state, country)
DO NOTHING;



-- COPY dim_store(store_name, city, state, country)
-- FROM 'C:/Users/VNAGASHA/datawarehousepoc/etl/source-data/stores.csv'
-- DELIMITER ',' CSV HEADER;