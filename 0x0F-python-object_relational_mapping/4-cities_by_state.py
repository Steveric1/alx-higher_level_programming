#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password and
database name. You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
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
    cursor = db.cursor()

    # execute mysql queries
    cursor.execute("""SELECT cities.id, cities.name, states.id FROM cities
                   INNER JOIN states ON cities.id = states.id
                   ORDER BY cities.id ASC""")
    states = cursor.fetchall()

    # loop through and print out the data in the table
    for state in states:
        print(state)

    # close connection to the database
    db.close()
