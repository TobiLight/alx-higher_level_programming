#!/usr/bin/python3
# File: 1-filter_states.py
# Author: Oluwatobiloba Light
"""
Lists all states with a `name` starting with the letter `N` from the
database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    q = db.cursor()
    q.execute("SELECT * FROM `states` WHERE `name` LIKE  BINARY 'N%'\
        ORDER BY 'states.id' ASC")
    [print(state) for state in q.fetchall()]
