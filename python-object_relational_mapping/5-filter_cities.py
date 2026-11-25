#!/usr/bin/python3
"""List the cities in the state supplied on the command line."""

import sys

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8mb4")
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT cities.name FROM cities "
                           "JOIN states ON cities.state_id = states.id "
                           "WHERE BINARY states.name = %s ORDER BY cities.id",
                           (sys.argv[4],))
            print(", ".join(city[0] for city in cursor.fetchall()))
    finally:
        db.close()
