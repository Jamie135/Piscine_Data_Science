import psycopg2


def main():
    """remove duplicates from customers table"""
    try:
        connection = psycopg2.connect(
            database="piscineds",
            user="pbureera",
            password="mysecretpassword",
            host="localhost",
            port="5432",
        )
        print("Connected to PostgreSQL Database")
        cursor = connection.cursor()
        cursor.execute("""CREATE TEMPORARY TABLE tmp AS
SELECT * FROM customers;

DELETE FROM tmp WHERE ctid IN (
SELECT ctid FROM (
    SELECT ctid, ROW_NUMBER() OVER(
            PARTITION BY date_trunc('minute', event_time),
            event_type,
            product_id,
            price,
            user_id,
            user_session ORDER BY event_time DESC
        ) AS row_num FROM customers
    ) AS duplicates WHERE duplicates.row_num > 1 );

DROP TABLE customers;

CREATE TABLE customers AS
SELECT *
FROM tmp
ORDER BY event_time;

DROP TABLE tmp;""")
        print("Query executed successfully")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
