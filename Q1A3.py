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
    db_path = './A3Small.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def smallSelfOptimized():
    global connection
    db_path = './A3Small.db'
    connect(db_path)

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def smallUserOptimized():
    global connection
    db_path = './A3Small.db'
    connect(db_path)

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def mediumUniformed():
    global connection
    db_path = './A3Medium.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def mediumSelfOptimized():
    global connection
    db_path = './A3Medium.db'
    connect(db_path)

    tic = time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    toc = time()
    exec_time =  tic - toc

    connection.commit()
    connection.close()

    return exec_time

def mediumUserOptimized():
    global connection
    db_path = './A3Medium.db'
    connect(db_path)

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def largeUniformed():
    global connection
    db_path = './A3Large.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def largeSelfOptimized():
    global connection
    db_path = './A3Large.db'
    connect(db_path)

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

    connection.commit()
    connection.close()

    return exec_time

def largeUserOptimized():
    global connection
    db_path = './A3Large.db'
    connect(db_path)

    init_time = datetime.datetime.now()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )
        
    end_time = datetime.datetime.now()
    exec_time =  end_time - init_time

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

    ax.bar(labels, uninformed, width, label="Uninformed")
    ax.bar(labels, self_optimized, width, label="Self Optimized")
    ax.bar(labels, user_optimized, width, label="User Optimized")

    ax.set_ylabel("Query runtime")
    ax.set_title("Query 1")
    ax.legend()

    tl = "Query_1"

    path = './{}_barchart.png'.format(tl)
    plt.savefig(path)
    print('Chart saved to file {}'.format(path))

    plt.close()
    return

    # print(one)
    # print(four)
    # print(seven)
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