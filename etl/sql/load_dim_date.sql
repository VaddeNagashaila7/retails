INSERT INTO dim_date (
    date_id,
    full_date,
    day,
    month,
    month_name,
    quarter,
    year,
    is_weekend
)
SELECT
    d::INT,
    to_date(d::TEXT,'YYYYMMDD'),
    EXTRACT(DAY FROM to_date(d::TEXT,'YYYYMMDD')),
    EXTRACT(MONTH FROM to_date(d::TEXT,'YYYYMMDD')),
    TO_CHAR(to_date(d::TEXT,'YYYYMMDD'),'Month'),
    EXTRACT(QUARTER FROM to_date(d::TEXT,'YYYYMMDD')),
    EXTRACT(YEAR FROM to_date(d::TEXT,'YYYYMMDD')),
    CASE 
        WHEN EXTRACT(DOW FROM to_date(d::TEXT,'YYYYMMDD')) IN (0,6) 
        THEN TRUE ELSE FALSE 
    END
FROM generate_series(20240101,20240131,1) d
ON CONFLICT (date_id)
DO NOTHING;









-- INSERT INTO dim_date
-- SELECT
--     d::INT,
--     to_date(d::TEXT,'YYYYMMDD'),
--     EXTRACT(DAY FROM to_date(d::TEXT,'YYYYMMDD')),
--     EXTRACT(MONTH FROM to_date(d::TEXT,'YYYYMMDD')),
--     TO_CHAR(to_date(d::TEXT,'YYYYMMDD'),'Month'),
--     EXTRACT(QUARTER FROM to_date(d::TEXT,'YYYYMMDD')),
--     EXTRACT(YEAR FROM to_date(d::TEXT,'YYYYMMDD')),
--     CASE WHEN EXTRACT(DOW FROM to_date(d::TEXT,'YYYYMMDD')) IN (0,6) THEN TRUE ELSE FALSE END
-- FROM generate_series(20240101,20240131,1) d;