import os
import psycopg2
import subprocess


def main():
    """create a table for all data_202*_***.csv files"""
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
        path = "/mnt/nfs/homes/pbureera/sgoinfre/eval/customer/"
        connection.autocommit = True
        cursor = connection.cursor()
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            subprocess.run(
                ["docker", "cp", file_path, f"postgres:/tmp/{file}"]
                )
            table = os.path.splitext(file)[0]
            create = f"""CREATE TABLE IF NOT EXISTS {table} (
                event_time TIMESTAMP,
                event_type VARCHAR(255),
                product_id INT,
                price FLOAT,
                user_id BIGINT,
                user_session UUID
                );
                COPY {table} FROM '/tmp/{table}.csv' CSV HEADER;
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
