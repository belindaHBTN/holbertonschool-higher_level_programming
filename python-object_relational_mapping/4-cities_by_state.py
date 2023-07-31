#!/usr/bin/python3
"""Lists all values in the states table where name match arg"""

import MySQLdb
from sys import argv


def get_state(username, password, db_name):
    """Lists all values in the states table where name match arg"""
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=db_name
    )
    cursor = db.cursor()

    cursor.execute(
            "SELECT c.id, c.name, s.name\
            FROM cities c\
            LEFT JOIN states s\
            ON c.state_id=s.id\
            ORDER BY c.id;"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_state(argv[1], argv[2], argv[3])
