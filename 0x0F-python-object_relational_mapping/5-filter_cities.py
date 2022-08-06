#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM states, \
    JOIN cities ON cities.state_id = states.id WHERE states.name = %s \
    ORDER BY cities.id ASC", [argv[4]])
    new = []

    for state in cur.fetchall():
        new += state
    print(', '.join(new))
    cur.close()

    db.close()
