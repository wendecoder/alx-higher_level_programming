#!/usr/bin/python3

"""
A script that lists all the cities in the ascending order of their id
username, password and database name are passed as user args
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

    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities, states WHERE cities.state_id = states.id")

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
