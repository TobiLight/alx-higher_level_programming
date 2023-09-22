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
    db_connect = db.connect(user=sys.argv[1], passwd=sys.argv[2],
                            db=sys.argv[3],  port=3306)

    q = db_connect.cursor()
    q.execute(
        "SELECT * FROM `states` ORDER BY 'states.id' ASC")

    [print(state) for state in q.fetchall() if state[1] == sys.argv[4]]
