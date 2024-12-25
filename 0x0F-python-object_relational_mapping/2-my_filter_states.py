#!/usr/bin/python3
'''
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'"
                "ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for j in rows:
        print(j)

    cur.close()
    db.close()
