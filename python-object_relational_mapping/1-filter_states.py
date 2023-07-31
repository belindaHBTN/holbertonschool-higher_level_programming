#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N) from the database"""

import MySQLdb
from sys import argv


def get_state(username, password, db_name):
    """ Lists all states from the database"""
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=db_name
    )
    cursor = db.cursor()

    cursor.execute(
            "SELECT id, name FROM states\
                    WHERE name LIKE BINARY 'N%' ORDER BY id;"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_state(argv[1], argv[2], argv[3])
