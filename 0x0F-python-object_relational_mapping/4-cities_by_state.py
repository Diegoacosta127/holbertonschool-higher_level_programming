#!/usr/bin/python3
"""module doc"""
import MySQLdb
from sys import argv


db = MySQLdb.connect(host='localhost',
                     user=argv[1],
                     passwd=argv[2],
                     db=argv[3],
                     port=3306)
cur = db.cursor()
cur.execute("SELECT cities.id, cities.name,\
            states.name FROM cities\
            JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC")
result = cur.fetchall()
if result:
    for i in result:
        print(i)
