#!/usr/bin/python3
# File: 3-my_safe_filter_states.py
# Author: Oluwatobiloba Light
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches
the argument
"""

import MySQLdb as db
import sys


if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=sys.argv[1], passwd=sys.argv[2],
                            db=sys.argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC",
        {'name': sys.argv[4]})

    print([print(state) for state in db_cursor.fetchall()])
