from .db_connection import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
SELECT date_id FROM dim_date
""")

existing = {row[0] for row in cur.fetchall()}

for d in range(20240101, 20240132):
    if d not in existing:
        cur.execute("""
        INSERT INTO dim_date VALUES (
            %s,
            to_date(%s::text,'YYYYMMDD'),
            EXTRACT(DAY FROM to_date(%s::text,'YYYYMMDD')),
            EXTRACT(MONTH FROM to_date(%s::text,'YYYYMMDD')),
            TO_CHAR(to_date(%s::text,'YYYYMMDD'),'Month'),
            EXTRACT(QUARTER FROM to_date(%s::text,'YYYYMMDD')),
            EXTRACT(YEAR FROM to_date(%s::text,'YYYYMMDD')),
            CASE WHEN EXTRACT(DOW FROM to_date(%s::text,'YYYYMMDD')) IN (0,6) THEN TRUE ELSE FALSE END
        )
        """, (d, d, d, d, d, d, d))

conn.commit()
cur.close()
conn.close()

print(" dim_date loaded")











# from datetime import date, timedelta
# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# start_date = date(2024, 1, 1)
# end_date = date(2024, 1, 31)

# current = start_date
# while current <= end_date:
#     cur.execute(
#         """
#         INSERT INTO dim_date
#         (date_id, full_date, day, month, month_name, quarter, year, is_weekend)
#         VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
#         ON CONFLICT (date_id) DO NOTHING
#         """,
#         (
#             int(current.strftime('%Y%m%d')),
#             current,
#             current.day,
#             current.month,
#             current.strftime('%B'),
#             (current.month - 1) // 3 + 1,
#             current.year,
#             current.weekday() >= 5
#         )
#     )
#     current += timedelta(days=1)

# conn.commit()
# cur.close()
# conn.close()

# print("✅ dim_date loaded")