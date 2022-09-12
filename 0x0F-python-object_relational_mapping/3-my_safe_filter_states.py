#!/usr/bin/python3

"""
A script that searches for a specific rows that contain the search term
while checking the passed string does not contain another stuff
username, password, database name and search term are passed as user args
"""

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

