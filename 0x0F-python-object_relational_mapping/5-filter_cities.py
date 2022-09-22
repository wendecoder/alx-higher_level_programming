#!/usr/bin/python3

"""
A script that prints cities that found in a specific state
username, password, database name and state name are passed as user args
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

    cursor.execute("SELECT cities.name FROM cities, states WHERE\
            cities.state_id = states.id and\
            states.name = %s", (sys.argv[4],))
    cities = cursor.fetchall()
    i = len(cities) - 1
    j = 0
    chrc = ''

    for city in cities:
        if j < i:
            for row in city:
                chrc += row + ", "
        else:
            for row in city:
                chrc += row
        j += 1
    print(chrc)

    cursor.close()
    db.close()
