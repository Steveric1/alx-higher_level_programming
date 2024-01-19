#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password
database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
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

    # # Executing the cursor to retrieve states from argument
    usr_arg = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (usr_arg,))
    states = cur.fetchall()

    # loop through and print out the data in the table
    for state in states:
        print(state)

    # close connection to the database
    db.close()
