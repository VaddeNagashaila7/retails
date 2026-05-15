import csv
from .db_connection import get_connection

conn = get_connection()
cur = conn.cursor()

with open('etl/source-data/customers.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        key = (
            row['customer_name'],
            row['gender'],
            row['city'],
            row['state'],
            row['country']
        )

        cur.execute("""
            SELECT 1 FROM dim_customer
            WHERE customer_name=%s AND gender=%s AND city=%s AND state=%s AND country=%s
        """, key)

        if not cur.fetchone():
            cur.execute("""
                INSERT INTO dim_customer(customer_name, gender, city, state, country)
                VALUES (%s, %s, %s, %s, %s)
            """, key)

conn.commit()
cur.close()
conn.close()

print("dim_customer loaded")


















# import csv
# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# with open('etl/source-data/products.csv', 'r') as f:
#     reader = csv.DictReader(f)
    
#     for row in reader:
#         cur.execute(
#             """
#             INSERT INTO dim_product
#             (product_name, category, subcategory, unit_price)
#             VALUES (%s, %s, %s, %s)
#             ON CONFLICT (product_name, category, subcategory, unit_price)
#             DO NOTHING;
#             """,
#             (
#                 row['product_name'],
#                 row['category'],
#                 row['subcategory'],
#                 row['unit_price']
#             )
#         )

# conn.commit()
# cur.close()
# conn.close()

# print("✅ dim_product loaded")