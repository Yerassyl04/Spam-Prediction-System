import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="Spam", user="postgres", password="admin", host="localhost", port="5432"
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error connecting to the database: {e}")
        raise
