import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config()
        print('connecting to PostgreSQL DB...')
        conn = psycopg2.connect(**params)
        print(params)

        cur = conn.cursor()

        print('PostgreSQL db version:')
        cur.execute('Select Version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('DB connection is closed')

if __name__ == '__main__':
    connect()