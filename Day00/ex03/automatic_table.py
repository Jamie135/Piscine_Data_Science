
import os
import pandas as pd
import psycopg2
from psycopg2 import OperationalError


def connect():
    """return a connection object with fixed parameters"""
    connection = psycopg2.connect(
        database="piscineds",
        user="pbureera",
        password="mysecretpassword",
        host="localhost",
        port="5432",
    )
    return connection


def load(path: str):
    """load a data file using pandas library"""
    assert isinstance(path, str), "your path is not valid."
    assert os.path.exists(path), "your file doesn't exist."
    assert os.path.isfile(path), "your 'file' is not a file."
    assert path.lower().endswith(".csv"), "file format is not .csv."
    data = pd.read_csv(path)
    print(f"Loading dataset of dimensions {data.shape}")

    return data


def main():
    """create a table"""
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""CREATE SCHEMA IF NOT EXISTS customers""")
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
        # open a cursor to perform database operations
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
