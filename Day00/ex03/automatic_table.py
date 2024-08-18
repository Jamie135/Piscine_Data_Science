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
        cursor.close()
        connection.close()
    except AssertionError as a:
        print(f"AssertionError: {a}")
    except OperationalError as e:
        print(f"OperationalError: {e}")


if __name__ == "__main__":
    main()
