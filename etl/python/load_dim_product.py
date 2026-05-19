
from .base_loader import BaseLoader

class DimProductLoader(BaseLoader):

    def __init__(self):
        super().__init__('etl/source-data/products.csv')

    def load(self):
        data = self.read_csv()

        for row in data:
            key = (
                row['product_name'],
                row['category'],
                row['subcategory'],
                float(row['unit_price'])
            )

            exists_query = """
                SELECT 1 FROM dim_product
                WHERE product_name=%s AND category=%s AND subcategory=%s AND unit_price=%s
            """

            if not self.record_exists(exists_query, key):
                insert_query = """
                    INSERT INTO dim_product
                    (product_name, category, subcategory, unit_price)
                    VALUES (%s, %s, %s, %s)
                """
                self.insert_record(insert_query, key)

        self.close()


if __name__ == "__main__":
    loader = DimProductLoader()
    loader.load()
    print("dim_product loaded")








































# import csv
# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# with open('etl/source-data/products.csv', 'r') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         key = (
#             row['product_name'],
#             row['category'],
#             row['subcategory'],
#             float(row['unit_price'])
#         )

#         cur.execute("""
#             SELECT 1 FROM dim_product
#             WHERE product_name=%s AND category=%s AND subcategory=%s AND unit_price=%s
#         """, key)

#         if not cur.fetchone():
#             cur.execute("""
#                 INSERT INTO dim_product(product_name, category, subcategory, unit_price)
#                 VALUES (%s, %s, %s, %s)
#             """, key)

# conn.commit()
# cur.close()
# conn.close()

# print("dim_product loaded")





















