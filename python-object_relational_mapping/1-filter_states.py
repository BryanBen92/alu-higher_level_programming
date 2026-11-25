#!/usr/bin/python3
"""List states whose names start with uppercase N."""

import sys

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8mb4")
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT id, name FROM states "
                           "WHERE BINARY name LIKE 'N%' ORDER BY id")
            for state in cursor.fetchall():
                print(state)
    finally:
        db.close()
