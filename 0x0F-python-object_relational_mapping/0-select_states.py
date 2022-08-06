#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
<<<<<<< HEAD
    cur.execute("SELECT * FROM states")
=======
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
>>>>>>> 34c2852b22f36a7e4e85ecc147247d4febc62ade
    [print(state) for state in cur.fetchall()]
    db.close()
    cur.close()
