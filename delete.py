import psycopg2
from config import config

def delete_part(part_id):
    conn = None
    rows_deleted = 0

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        sql = """DELETE FROM parts WHERE part_id = %s"""
        cur.execute(sql, (part_id,))
        rows_deleted = cur.rowcount

        conn.commit()
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    delete_part(4)