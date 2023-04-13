#!/usr/bin/python3
"""Select states"""
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
cur.execute("SELECT * FROM states")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
