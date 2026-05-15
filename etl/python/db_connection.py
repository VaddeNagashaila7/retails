import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="retail_dw",
        user="postgres",
        password="30036681"
    )
