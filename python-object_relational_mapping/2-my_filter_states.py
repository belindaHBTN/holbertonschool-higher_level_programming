#!/usr/bin/python3
"""Display all values in states table that matche the search name"""

import MySQLdb
from sys import argv


def get_state(username, password, db_name, search_name):
    """Display all values in states table that matche the search name"""
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=db_name
    )
    cursor = db.cursor()

    cursor.execute(
            "SELECT id, name FROM states WHERE name LIKE BINARY '{}'\
                    ORDER BY id;".format(search_name)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_state(argv[1], argv[2], argv[3], argv[4])
