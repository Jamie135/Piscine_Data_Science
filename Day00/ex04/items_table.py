import os
import psycopg2
import subprocess


def main():
    """create a table for item.csv file"""
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
        path = "/mnt/nfs/homes/pbureera/sgoinfre/subject/item/"
        connection.autocommit = True
        cursor = connection.cursor()
        file_path = os.path.join(path, "item.csv")
        subprocess.run(
            ["docker", "cp", file_path, "postgres:/tmp/item.csv"]
            )
        create = """CREATE TABLE IF NOT EXISTS items (
            product_id INT,
            category_id BIGINT,
            category_code VARCHAR(255),
            brand VARCHAR(255)
            );
            COPY items FROM '/tmp/item.csv' CSV HEADER;
            """
        cursor.execute(create)
        subprocess.run(
            ["docker", "exec", "postgres", "rm", "/tmp/item.csv"]
            )
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
