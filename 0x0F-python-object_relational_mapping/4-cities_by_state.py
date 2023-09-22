#!/usr/bin/python3
# File: 4-cities_by_state.py
# Author: Oluwatobiloba Light
"""
Lists all cities from the database `hbtn_0e_4_usa`.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    q = db.cursor()
    q.execute("SELECT cities.id, cities.name, states.name FROM `cities`\
        JOIN states on cities.state_id = states.id ORDER BY 'cities.id' ASC")
    [print(city) for city in q.fetchall()]
