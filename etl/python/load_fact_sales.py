import csv
from .db_connection import get_connection

conn = get_connection()
cur = conn.cursor()

with open('etl/source-data/sales.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        key = (
            int(row['date_id']),
            int(row['customer_id']),
            int(row['product_id']),
            int(row['store_id'])
        )

        cur.execute("""
            SELECT 1 FROM fact_sales
            WHERE date_id=%s AND customer_id=%s AND product_id=%s AND store_id=%s
        """, key)

        if not cur.fetchone():
            cur.execute("""
                INSERT INTO fact_sales(date_id, customer_id, product_id, store_id, quantity, sales_amount)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                key[0], key[1], key[2], key[3],
                int(row['quantity']),
                float(row['sales_amount'])
            ))

conn.commit()
cur.close()
conn.close()

print("✅ fact_sales loaded")












# import csv
# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# with open('etl/source-data/sales.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         cur.execute(
#             """
#             INSERT INTO fact_sales
#             (date_id, customer_id, product_id, store_id, quantity, sales_amount)
#             VALUES (%s,%s,%s,%s,%s,%s)
#             """,
#             (
#                 row['date_id'],
#                 row['customer_id'],
#                 row['product_id'],
#                 row['store_id'],
#                 row['quantity'],
#                 row['sales_amount']
#             )
#         )

# conn.commit()
# cur.close()
# conn.close()

# print("✅ fact_sales loaded")