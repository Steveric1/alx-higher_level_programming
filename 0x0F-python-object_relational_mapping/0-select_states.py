#!/usr/bin/python3

import sys
import MySQLdb


def list_all():
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
    print()

    # close connection to the database
    db.close()


if __name__ == "__main__":
    list_all()
