import psycopg2
from config import config

def get_parts():
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = """SELECT part_id, part_name FROM parts ORDER BY part_name DESC """
        cur.execute(sql)

        rows = cur.fetchall()
        print("the number of parts:", cur.rowcount)

        for row in rows:
            print(row)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    get_parts()