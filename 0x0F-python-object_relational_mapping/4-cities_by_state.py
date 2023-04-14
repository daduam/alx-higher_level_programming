#!/usr/bin/python3
"""Lists all cities with their corresponding state"""
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
    SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
