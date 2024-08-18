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
        print("Connected to PostgreSQL Database")
        with open("automatic_table.sql", "r") as sql:
            query = sql.read()
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(query)
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except OperationalError as o:
        print(f"OperationalError: {o}")
    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
