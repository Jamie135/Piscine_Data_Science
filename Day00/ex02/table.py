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
        with open("table.sql", "r") as sql:
            query = sql.read()
        # allow each executed SQL query to not be rolled back
        # when closing the connection 
        connection.autocommit = True
        # open a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute(query)
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except OperationalError as o:
        print(f"Error: {o}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
