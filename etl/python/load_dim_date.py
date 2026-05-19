from .base_loader import BaseLoader

class DimDateLoader(BaseLoader):

    def __init__(self):
        # No CSV file needed, we generate dates internally
        super().__init__(file_path=None)

    def load(self):
        # Step 1: Get existing date_ids
        self.cur.execute("SELECT date_id FROM dim_date")
        existing_dates = {row[0] for row in self.cur.fetchall()}

        # Step 2: Generate date range (Jan 2024 example)
        for d in range(20240101, 20240132):

            # Skip if already exists
            if d in existing_dates:
                continue

            # Step 3: Insert new date
            self.cur.execute("""
                INSERT INTO dim_date (
                    date_id, full_date, day, month, month_name,
                    quarter, year, is_weekend
                )
                VALUES (
                    %s,
                    to_date(%s::text, 'YYYYMMDD'),
                    EXTRACT(DAY FROM to_date(%s::text, 'YYYYMMDD')),
                    EXTRACT(MONTH FROM to_date(%s::text, 'YYYYMMDD')),
                    TO_CHAR(to_date(%s::text, 'YYYYMMDD'), 'Month'),
                    EXTRACT(QUARTER FROM to_date(%s::text, 'YYYYMMDD')),
                    EXTRACT(YEAR FROM to_date(%s::text, 'YYYYMMDD')),
                    CASE 
                        WHEN EXTRACT(DOW FROM to_date(%s::text, 'YYYYMMDD')) IN (0,6)
                        THEN TRUE ELSE FALSE
                    END
                )
            """, (d, d, d, d, d, d, d))

        self.close()


if __name__ == "__main__":
    loader = DimDateLoader()
    loader.load()
    print(" dim_date loaded ")





















































































































# from .db_connection import get_connection

# conn = get_connection()
# cur = conn.cursor()

# cur.execute("""
# SELECT date_id FROM dim_date
# """)

# existing = {row[0] for row in cur.fetchall()}

# for d in range(20240101, 20240132):
#     if d not in existing:
#         cur.execute("""
#         INSERT INTO dim_date VALUES (
#             %s,
#             to_date(%s::text,'YYYYMMDD'),
#             EXTRACT(DAY FROM to_date(%s::text,'YYYYMMDD')),
#             EXTRACT(MONTH FROM to_date(%s::text,'YYYYMMDD')),
#             TO_CHAR(to_date(%s::text,'YYYYMMDD'),'Month'),
#             EXTRACT(QUARTER FROM to_date(%s::text,'YYYYMMDD')),
#             EXTRACT(YEAR FROM to_date(%s::text,'YYYYMMDD')),
#             CASE WHEN EXTRACT(DOW FROM to_date(%s::text,'YYYYMMDD')) IN (0,6) THEN TRUE ELSE FALSE END
#         )
#         """, (d, d, d, d, d, d, d))

# conn.commit()
# cur.close()
# conn.close()

# print(" dim_date loaded")











