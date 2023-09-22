#!/usr/bin/python3
# File: 5-filter_cities.py
# Author: Oluwatobiloba Light
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Access to the database and get the cities of a state
    from the database.
    """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    q = db.cursor()
    q.execute("""
              SELECT
                cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY '{}'
            ORDER BY
                cities.id ASC
        """.format(sys.argv[4]))
    print(", ".join([city[0] for city in q.fetchall()]))
