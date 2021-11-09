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
#    cursor.execute(' PRAGMA automatic_index = boolean; ')

    connection.commit()
    return

def main():
    global connection
    
#    db_path = PASS
#    connect(db_path)

    connection.close()
  
if __name__ == "__main__":
    main()