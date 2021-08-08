#!/usr/bin/python3
"""
Script that lists all cities of a state given as an argument
from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    SQL = "SELECT cities.name\
           FROM cities\
           INNER JOIN states\
           ON cities.state_id = states.id\
           WHERE BINARY states.name = %(username)s\
           ORDER BY cities.id ASC"
    cursor.execute(SQL, {'username': sys.argv[4]})
    cities = cursor.fetchall()
    if cities is not None:
        for index, value in enumerate(cities):
            if index != len(cities) - 1:
                print("{}, ".format(value[0]), end="")
            else:
                print("{}".format(value[0]))
    else:
        print("")
    cursor.close()
    db.close()
