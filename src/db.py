import psycopg2
import os
from psycopg2 import Error

def get_db_connection():
    connection = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=os.environ.get("POSTGRES_USER"),
                                    password=os.environ.get("POSTGRES_PASSWORD"),
                                    host="db",
                                    port="5432")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")