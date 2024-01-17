#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
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
    cursor = db.cursor()

    # execute mysql queries
    cursor.execute("SELECT * FROM states ORDER BY id;")
    states = cursor.fetchall()

    # loop through and print out the data in the table
    for state in states:
        print(state)

    # close connection to the database
    db.close()
