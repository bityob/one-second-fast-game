#!/usr/bin/env python

# Number to guess: How many times can we
# select a row from an **unindexed** table with 
# 10,000,000 rows?

import sqlite3

conn = sqlite3.connect('./unindexed_db.sqlite')
c = conn.cursor()
def f(NUMBER):
    query = "select * from my_table where key = %d" % 5
    for i in range(NUMBER):
        c.execute(query)
        c.fetchall()

if __name__ == '__main__':
    import sys
    f(int(sys.argv[1]))
