#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute(f"SELECT * FROM states WHERE name = '{sys.argv[4]}'  ORDER BY id ASC")
    data = curr.fetchall()
    for row in data:
        print(row)
