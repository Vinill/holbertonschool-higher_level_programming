#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM states, \
    JOIN cities ON cities.state_id = states.id WHERE states.name = %s \
    ORDER BY cities.id ASC", [argv[4]])
    new = []

    [print(', '.join(new) for state in cur.fetchall() new += state]
    cur.close()
    db.close()
