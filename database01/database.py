#!/usr/bin/env python

#############################################################################
## 2011 YS
##
#############################################################################

import sqlite3   
import math
import os, sys
import traceback

def connect_data_base(str_db_name):
    con = sqlite3.connect(str_db_name)
    cur = con.cursor()
    return cur, con

def create_table(cur, con):
    # Create Item table
    # cur.execute('CREATE TABLE foo (o_id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30))')    
    cur.execute('''create table my_table_item
                    (id integer primary key, itemno text unique,
                     scancode text, descr text, price real)''')    
    con.commit()

def insert_table(cur, con):
    # cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
    # cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "cherry", "melony")')
    #cur.execute("INSERT INTO my_table_item VALUES (NULL,0001,32187645,'Milk',2.50)")
    #cur.execute("INSERT INTO my_table_item VALUES (NULL,0002,45321876,'Beer',4.50)")
    #cur.execute("INSERT INTO my_table_item VALUES (NULL,0003,18764532,'Bread',1.50)")
    #cur.execute("INSERT INTO my_table_item VALUES (NULL,0004,384564532,'Tomato',3.35)")
   #cur.execute("INSERT INTO my_table_item VALUES (NULL,0005,988654325,'Makkara',8.44)")
    cur.execute("INSERT INTO my_table_item VALUES (NULL,0007,67435367,'Veen',4.50)")
    
    con.commit()
    print cur.lastrowid

def get_table(cur, str_to_exec):
    cur.execute(str_to_exec)
    return cur.fetchall()

if __name__ == "__main__":    

    print "Main program start."
    print ""
    # string_to_execute = 'SELECT * FROM foo WHERE fruit="cherry"'
    # string_to_execute = 'SELECT * FROM foo'
    # string_to_execute = 'SELECT * FROM my_table_item'
    string_to_execute = 'SELECT * FROM my_table_item WHERE price=8.44'
    # string_db_name = 'mydatabase.db'
    string_db_name = 'foodgiant.db'
    
    try:
        cursor_db, connect_db = connect_data_base(string_db_name)
        #create_table(cursor_db, connect_db)
        # insert_table(cursor_db, connect_db)
        db_result =  get_table(cursor_db, string_to_execute)
        for row in db_result:
            print row[1], row[2], row[3], row[4]

    except:
        print "1. Error occures: unknown"
        traceback.print_exc()    
    print "Main program ends"



