
import csv
from .db_connection import get_connection

class BaseLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def read_csv(self):
        with open(self.file_path, 'r') as f:
            return list(csv.DictReader(f))

    def record_exists(self, query, values):
        self.cur.execute(query, values)
        return self.cur.fetchone() is not None

    def insert_record(self, query, values):
        self.cur.execute(query, values)

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
