import psycopg2
from psycopg2 import OperationalError


def main():
    """create a table"""
    try:
        connection = psycopg2.connect(
            database="piscineds",
            user="pbureera",
            password="mysecretpassword",
            host="localhost",
            port="5432",
        )
        query = """
            CREATE TABLE IF NOT EXISTS data_2022_oct (
            event_time TIMESTAMPTZ,
            event_type VARCHAR,
            product_id INTEGER,
            price FLOAT,
            user_id BIGINT,
            user_session UUID
            )
        """
        # allow each executed SQL query to not be rolled back
        # when closing the connection 
        connection.autocommit = True
        # open a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        connection.close()
    except OperationalError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
