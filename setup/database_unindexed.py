#!/usr/bin/env python

# Number to guess: How many times can we
# select a row from an indexed table with 
# 1,000,000 rows?

import sqlite3
import os
try:
    os.remove('./unindexed_db.sqlite')
except:
    pass
conn = sqlite3.connect('./unindexed_db.sqlite')
c = conn.cursor()
c.execute("create table my_table (key integer, s string)")

elements = [(i, str(i)) for i in range(10**7)]
c.executemany('INSERT INTO my_table VALUES (?,?)', elements)
conn.commit()

