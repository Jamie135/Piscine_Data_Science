import os
import psycopg2
import subprocess
import pandas as pd


def main():
    """create customers table"""
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
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            data = pd.read_csv(file_path, nrows=1)
            columns_lst = data.columns.to_list()
            columns = (" ,").join(columns_lst)
            subprocess.run(
                ["docker", "cp", file_path, f"postgres:/tmp/{file}"]
                )
            create = f"""CREATE TABLE IF NOT EXISTS customers (
                event_time TIMESTAMP,
                event_type VARCHAR(255),
                product_id INT,
                price FLOAT,
                user_id BIGINT,
                user_session UUID
                );
                COPY customers({columns}) FROM '/tmp/{file}' CSV HEADER;
                """
            cursor.execute(create)
            subprocess.run(
                ["docker", "exec", "postgres", "rm", f"/tmp/{file}"]
                )
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


# SELECT * FROM customers WHERE EXTRACT(YEAR FROM event_time) > 2022;
