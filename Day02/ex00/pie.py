import psycopg2
import matplotlib.pyplot as plt


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
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("""SELECT event_type, COUNT(*)
FROM customers
GROUP BY event_type
ORDER BY COUNT(event_type) DESC;""")
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        event_type, count = zip(*data)
        plt.pie(count, labels=event_type, autopct="%1.1f%%")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
