#!/usr/bin/python3
# File: 0-select_states.py
# Author: Oluwatobiloba Light
# Lists all states from the database hbtn_0e_0_usa
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    q = db.cursor()
    q.execute("SELECT * FROM `states`")
    [print(state) for state in q.fetchall()]
