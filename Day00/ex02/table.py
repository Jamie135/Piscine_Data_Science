import os
import psycopg2
import subprocess


def main():
    """create a table for data_2022_oct.csv file"""
    try:
        connection = psycopg2.connect(
            database="piscineds",
            user="pbureera",
            password="mysecretpassword",
            host="localhost",
            port="5432",
        )
        print("Connected to PostgreSQL Database")
        # path = os.path.expanduser("~/Documents/42/Data/subject/customer")
        path = "/mnt/nfs/homes/pbureera/sgoinfre/subject/customer/"
        connection.autocommit = True
        cursor = connection.cursor()
        file_path = os.path.join(path, "data_2022_oct.csv")
        subprocess.run(
            ["docker", "cp", file_path, "postgres:/tmp/data_2022_oct.csv"]
            )
        create = """CREATE TABLE IF NOT EXISTS data_2022_oct (
            event_time TIMESTAMP,
            event_type VARCHAR(255),
            product_id INT,
            price FLOAT,
            user_id BIGINT,
            user_session UUID
            );
            COPY data_2022_oct FROM '/tmp/data_2022_oct.csv' CSV HEADER;
            """
        cursor.execute(create)
        subprocess.run(
            ["docker", "exec", "postgres", "rm", "/tmp/data_2022_oct.csv"]
            )
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
