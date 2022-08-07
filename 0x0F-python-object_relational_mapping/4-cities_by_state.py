#!/usr/bin/python3
"""Task: 0. Get all states"""

import MySQLdb
from sys import argv

if (__name__ == "__main__"):
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    cur = con.cursor()
    qryOne = "SELECT cities.id, cities.name, states.name FROM cities"
    qryTwo = " INNER JOIN states ON cities.state_id = states.id"
    cur.execute(qryOne + qryTwo)
    query = cur.fetchall()

    for x in query:
        print(x)
    cur.close()
    con.close()
