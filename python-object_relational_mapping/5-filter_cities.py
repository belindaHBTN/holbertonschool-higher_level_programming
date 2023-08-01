#!/usr/bin/python3
"""Lists all cities of a selected state from the database"""

import MySQLdb
from sys import argv


def get_state(username, password, db_name, state_name):
    """Lists all cities of a selected state from the database"""
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=db_name
    )
    cursor = db.cursor()

    cursor.execute(
            "SELECT c.name\
            FROM cities c\
            LEFT JOIN states s\
            ON c.state_id=s.id\
            WHERE s.name LIKE %s\
            ORDER BY c.id;", (state_name, )
    )
    rows = cursor.fetchall()
    city_list = []
    for row in rows:
        city_list.append(row[0])
    city_str = ", ".join(city_list)
    print(city_str)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_state(argv[1], argv[2], argv[3], argv[4])
