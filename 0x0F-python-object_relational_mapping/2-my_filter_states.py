#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    state = sys.argv[4]
    query = """
    SELECT * FROM states
    WHERE BINARY name = '{}' ORDER BY states.id ASC
    """
    cur.execute(query.format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
