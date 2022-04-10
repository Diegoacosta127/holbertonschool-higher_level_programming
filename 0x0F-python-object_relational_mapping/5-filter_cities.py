#!/usr/bin/python3
"""module doc"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id=states.id\
                WHERE states.name LIKE %s\
                ORDER BY cities.id ASC", (argv[4],))
    result = cur.fetchall()
    if len(result) > 0:
        for i in range(len(result)):
            if (i != len(result) - 1):
                print(str(result[i]).strip('(\',\')'), end=', ')
            else:
                print(str(result[i]).strip('(\',\')'))
    else:
        print()
