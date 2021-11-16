import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from time import time 
import datetime

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
    import time
    db_path = './A3Small.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def smallSelfOptimized():
    global connection
    import time
    db_path = './A3Small.db'
    connect(db_path)

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def smallUserOptimized():
    global connection
    import time
    db_path = './A3Small.db'
    connect(db_path)

    init_time = datetime.datetime.now()

    cursor.execute(" ")

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def mediumUniformed():
    global connection
    import time
    db_path = './A3Medium.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def mediumSelfOptimized():
    global connection
    import time
    db_path = './A3Medium.db'
    connect(db_path)

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def mediumUserOptimized():
    global connection
    import time
    db_path = './A3Medium.db'
    connect(db_path)

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def largeUniformed():
    global connection
    import time
    db_path = './A3Large.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def largeSelfOptimized():
    global connection
    import time
    db_path = './A3Large.db'
    connect(db_path)

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def largeUserOptimized():
    global connection
    import time
    db_path = './A3Large.db'
    connect(db_path)

    start_time=time.time()

    for i in range(50):
        cursor.execute(" " )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    return exec_time

def bar_chart(one, two, three, four, five, six, seven, eight, nine):

    labels = ['SmallDB', 'MediumDB', 'LargeDB']
    
    uninformed = [one, four, seven]
    self_optimized = [two, five, eight]
    user_optimized = [three, six, nine]

    width = 0.4

    fig, ax = plt.subplots()

    uninformed=np.array(uninformed)
    self_optimized=np.array(self_optimized)
    user_optimized=np.array(user_optimized)

    ax.bar(labels, uninformed, width, label="Uninformed")
    ax.bar(labels, self_optimized, width, bottom = uninformed, label="Self Optimized")
    ax.bar(labels, user_optimized, width, bottom=uninformed+self_optimized, label="User Optimized")

    ax.set_ylabel("Query runtime in milliseconds")
    ax.set_title("Query 1")
    ax.legend()

    tl = "Query_1"

    path = './{}_barchart.png'.format(tl)
    plt.savefig(path)
    print('Chart saved to file {}'.format(path))

    plt.close()
    return

    # print(one)
    # print(two)
    # print(three)
    # print(four)
    # print(five)
    # print(six)
    # print(seven)
    # print(eight)
    # print(nine)
    # return

def main():
    global connection

    ######## Small Query information to pass to barchart ###########

    one = smallUniformed()
    two = smallSelfOptimized()
    three = smallUserOptimized()

    ######## Medium Query information to pass to barchart ###########

    four = mediumUniformed()
    five = mediumSelfOptimized()
    six = mediumUserOptimized()

    ######## Large Query information to pass to barchart ###########

    seven = largeUniformed()
    eight = largeSelfOptimized()
    nine = largeUserOptimized()

    ######## Pass information to barchart function ############

    bar_chart(one, two, three, four, five, six, seven, eight, nine)

    connection.close()
    print("Connection to database closed")
  
if __name__ == "__main__":
    main()