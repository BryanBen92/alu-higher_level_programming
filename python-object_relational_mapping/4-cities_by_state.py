#!/usr/bin/python3
"""List cities with their states in city ID order."""

import sys

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8mb4")
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT cities.id, cities.name, states.name "
                           "FROM cities JOIN states "
                           "ON cities.state_id = states.id "
                           "ORDER BY cities.id")
            for city in cursor.fetchall():
                print(city)
    finally:
        db.close()
