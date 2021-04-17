import psycopg2
from config import config

def get_vendors():
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        sql = """ SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name ASC """

        cur.execute(sql)
        print("the number of parts:", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_vendors()