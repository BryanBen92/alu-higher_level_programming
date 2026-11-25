#!/usr/bin/python3
"""List states whose names match a given value."""

import sys

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8mb4")
    try:
        with db.cursor() as cursor:
            state_name = db.literal(sys.argv[4]).decode(db.encoding)
            query = ("SELECT id, name FROM states WHERE BINARY name = {} "
                     "ORDER BY id").format(state_name)
            cursor.execute(query)
            for state in cursor.fetchall():
                print(state)
    finally:
        db.close()
