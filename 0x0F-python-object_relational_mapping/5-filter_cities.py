#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s", (sys.argv[4],))
    data = curr.fetchall()
    if data:
        print(', '.join(city[0] for city in data))
    else:
        print()
