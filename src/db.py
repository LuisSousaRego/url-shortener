import psycopg2
import os
from psycopg2 import Error

def setup_db():
    connection = None
    try:
        connection = psycopg2.connect(user=os.environ.get("POSTGRES_USER"),
                                    password=os.environ.get("POSTGRES_PASSWORD"),
                                    host="db",
                                    port="5432")

        cur = connection.cursor()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS urls (
                    url                 TEXT NOT NULL,
                    shortcode           char(6) PRIMARY KEY,
                    created             timestamp NOT NULL DEFAULT current_timestamp,
                    last_redirect       timestamp,
                    redirect_count      integer NOT NULL DEFAULT 0
                );""")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        connection.commit()
        cur.close()

    return connection