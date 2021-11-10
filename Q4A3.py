import sqlite3
import matplotlib.pyplot as plt
import numpy as np

connection = None
cursor = None

def connect(path):

    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(' PRAGMA foreign_keys=ON; ')

    connection.commit()
    return

def smallUniformed():
    global connection
    db_path = './A3Small.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def smallSelfOptimized():
    global connection
    db_path = './A3Small.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def smallUserOptimized():
    global connection
    db_path = './A3Small.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def mediumUniformed():
    global connection
    db_path = './A3Medium.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def mediumSelfOptimized():
    global connection
    db_path = './A3Medium.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def mediumUserOptimized():
    global connection
    db_path = './A3Medium.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def largeUniformed():
    global connection
    db_path = './A3Large.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def largeSelfOptimized():
    global connection
    db_path = './A3Large.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def largeUserOptimized():
    global connection
    db_path = './A3Large.db'
    connect(db_path)

    Query = '''


    '''

    connection.commit()
    connection.close()
    return

def bar_chart():
    
    print("Query 4 (runtime in ms)")

def main():
    global connection

    # Loop through functions 

    connection.close()
    print("Connection to database closed")
  
if __name__ == "__main__":
    main()