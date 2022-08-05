#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, states.name, cities.name FROM states, \
    cities WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
