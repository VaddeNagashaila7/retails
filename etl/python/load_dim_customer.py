
from .base_loader import BaseLoader

class DimCustomerLoader(BaseLoader):

    def __init__(self):
        super().__init__('etl/source-data/customers.csv')

    def load(self):
        data = self.read_csv()

        for row in data:
            key = (
                row['customer_name'],
                row['gender'],
                row['city'],
                row['state'],
                row['country']
            )

            exists_query = """
                SELECT 1 FROM dim_customer
                WHERE customer_name=%s AND gender=%s AND city=%s AND state=%s AND country=%s
            """

            if not self.record_exists(exists_query, key):
                insert_query = """
                    INSERT INTO dim_customer
                    (customer_name, gender, city, state, country)
                    VALUES (%s, %s, %s, %s, %s)
                """
                self.insert_record(insert_query, key)

        self.close()


if __name__ == "__main__":
    loader = DimCustomerLoader()
    loader.load()
    print(" dim_customer loaded")








































# import csv
# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# with open('etl/source-data/customers.csv', 'r') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         key = (
#             row['customer_name'],
#             row['gender'],
#             row['city'],
#             row['state'],
#             row['country']
#         )

#         cur.execute("""
#             SELECT 1 FROM dim_customer
#             WHERE customer_name=%s AND gender=%s AND city=%s AND state=%s AND country=%s
#         """, key)

#         if not cur.fetchone():
#             cur.execute("""
#                 INSERT INTO dim_customer(customer_name, gender, city, state, country)
#                 VALUES (%s, %s, %s, %s, %s)
#             """, key)

# conn.commit()
# cur.close()
# conn.close()

# print("dim_customer loaded")


















