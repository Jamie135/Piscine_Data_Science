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
        with open("remove_duplicates.sql", "r") as sql:
            query = sql.read()
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(query)
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
