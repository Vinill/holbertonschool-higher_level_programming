#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys 
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM states, \
    JOIN cities ON cities.state_id = states.id WHERE states.name = %s \
    ORDER BY cities.id ASC", [argv[4]])
    new = []

    for row in cur.fetchall():
        print(row[0], end=" ," if row != rows[-1] else "\n")

    db.close()
