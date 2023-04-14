#!/usr/bin/python3
"""Lists all cities of the supplied state"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=user,
                           passwd=passwd,
                           db=db,
                           charset="utf8")
    cur = conn.cursor()
    query = """
    SELECT name FROM cities
    WHERE state_id = (
        SELECT id FROM states
        WHERE name = %s
        LIMIT 1)
    ORDER BY cities.id
    """
    state = sys.argv[4]
    cur.execute(query, (state,))
    query_rows = cur.fetchall()
    rows = [x[0] for x in query_rows]
    print(*rows, sep=", ")
    cur.close()
    conn.close()
