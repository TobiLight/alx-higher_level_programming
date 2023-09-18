#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> <mysql password>
#        <database name>
# Author: Oluwatobiloba Light

import sys
import MySQLdb

if __name__ == "__main__":
    db_connect = MySQLdb.connect(
        host="localhost", user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.rgv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
