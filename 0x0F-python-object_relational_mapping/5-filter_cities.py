#!/usr/bin/python3
'''
Script that takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name "
                "FROM cities INNER JOIN states "
                "ON cities.state_id = states.id "
                "WHERE states.name = %s", (argv[4], ))
    city = cur.fetchall()
    x = [j[0] for j in city]
    cities_list = ", ".join(x)
    print(cities_list)
    cur.close()
    db.close()
