#!/usr/bin/python3

"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password and
database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # cursor to interact with the database queries
    cur = db.cursor()

    # # Executing the cursor to retrieve states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()

    # loop through and print out the data in the table
    for state in states:
        if state[1][0] == 'N':
            print(state)

    # close connection to the database
    db.close()
