import csv
from .db_connection import get_connection

conn = get_connection()
cur = conn.cursor()

with open('etl/source-data/stores.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        key = (
            row['store_name'],
            row['city'],
            row['state'],
            row['country']
        )

        cur.execute("""
            SELECT 1 FROM dim_store
            WHERE store_name=%s AND city=%s AND state=%s AND country=%s
        """, key)

        if not cur.fetchone():
            cur.execute("""
                INSERT INTO dim_store(store_name, city, state, country)
                VALUES (%s, %s, %s, %s)
            """, key)

conn.commit()
cur.close()
conn.close()

print("dim_store loaded")













# import csv
# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# with open('etl/source-data/stores.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         cur.execute(
#             """
#             INSERT INTO dim_store
#             (store_name, city, state, country)
#             VALUES (%s,%s,%s,%s)
#             """,
#             (
#                 row['store_name'],
#                 row['city'],
#                 row['state'],
#                 row['country']
#             )
#         )

# conn.commit()
# cur.close()
# conn.close()

# print("✅ dim_store loaded")