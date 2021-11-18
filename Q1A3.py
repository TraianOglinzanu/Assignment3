import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from time import time 

connection = None
cursor = None

def connect(path):

    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    cursor.execute(' PRAGMA foreign_keys=ON; ')

    connection.commit()
    return

def smallUninformed():
    global connection
    import time
    db_path = './A3Small2.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')
    cursor.execute(' PRAGMA automatic_index=false')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    cursor.execute(' PRAGMA foreign_keys=ON; ')
    cursor.execute(' PRAGMA automatic_index=true')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    # cursor.execute("CREATE INDEX my_customer_index ON Customers (customer_id)")
    # cursor.execute("CREATE INDEX my_order_index ON Orders (order_id)")

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000
  
    connection.commit()
    connection.close()

    # cursor.execute("DROP INDEX")

    return exec_time

def mediumUninformed():
    global connection
    import time
    db_path = './A3Medium2.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')
    cursor.execute(' PRAGMA automatic_index=false')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    cursor.execute(' PRAGMA foreign_keys=ON; ')
    cursor.execute(' PRAGMA automatic_index=true')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    # cursor.execute("CREATE INDEX customer_index ON Customers (customer_id)")
    # cursor.execute("CREATE INDEX order_index ON Orders (order_id)")

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000

    connection.commit()
    connection.close()

    return exec_time

def largeUninformed():
    global connection
    import time
    db_path = './A3Large2.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')
    cursor.execute(' PRAGMA automatic_index=false')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    cursor.execute(' PRAGMA foreign_keys=ON; ')
    cursor.execute(' PRAGMA automatic_index=true')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    # query1 = '''
    #                     CREATE TABLE Customers (
    #                     customer_id TEXT,
    #                     customer_postal_code INTEGER,
    #                     PRIMARY KEY(customer_id)
    #                     ) WITHOUT ROWID;
    #                 '''
    
    # query2 = '''
    #                 CREATE TABLE ORDERS (
    #                     order_id TEXT,
    #                     customer_id TEXT,
    #                     PRIMARY KEY(order_id)
    #                 ) WITHOUT ROWID;
    #                '''

    # cursor.execute(query1)
    # cursor.execute(query2)

    # cursor.execute("CREATE INDEX my_customer_id_index ON Customers (customer_id)")
                    
    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT COUNT(order_id) FROM Customers c, Orders o WHERE c.customer_id = o.customer_id  AND  customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000

    connection.commit()
    connection.close()

    return exec_time

def bar_chart(one, two, three, four, five, six, seven, eight, nine):

    # labels = ['SmallDB', 'MediumDB', 'LargeDB']
    
    # uninformed = [one, four, seven]
    # self_optimized = [two, five, eight]
    # user_optimized = [three, six, nine]

    # width = 0.4

    # fig, ax = plt.subplots()

    # uninformed=np.array(uninformed)
    # self_optimized=np.array(self_optimized)
    # user_optimized=np.array(user_optimized)

    # ax.bar(labels, uninformed, width, label="Uninformed")
    # ax.bar(labels, self_optimized, width, bottom = uninformed, label="Self Optimized")
    # ax.bar(labels, user_optimized, width, bottom=uninformed+self_optimized, label="User Optimized")

    # ax.set_ylabel("Query runtime in milliseconds")
    # ax.set_title("Query 1")
    # ax.legend()

    # tl = "Query_1"

    # path = './{}_barchart.png'.format(tl)
    # plt.savefig(path)
    # print('Chart saved to file {}'.format(path))

    # plt.close()
    # return

    # print("Small Unoptimized: " + str(one))
    # print("Small SelfOptimized: " + str(two))
    # print("Small UserOptimized: " + str(three))

    # print("Medium Unoptimized: " + str(four))
    # print("Medium SelfOptimized: " + str(five))
    # print("Medium UserOptimized: " + str(six))

    print("Large Uninformed: " + str(seven))
    print("Large Self-optimized: " + str(eight))
    print("Large User-optimized: " + str(nine))

    return

def main():
    global connection

    ######## Small Query information to pass to barchart ###########

    one = smallUninformed()
    two = smallSelfOptimized()
    three = smallUserOptimized()

    ######## Medium Query information to pass to barchart ###########

    four = mediumUninformed()
    five = mediumSelfOptimized()
    six = mediumUserOptimized()

    ######## Large Query information to pass to barchart ###########

    seven = largeUninformed()
    eight = largeSelfOptimized()
    nine = largeUserOptimized()

    ######## Pass information to barchart function ############

    bar_chart(one, two, three, four, five, six, seven, eight, nine)

    connection.close()
  
if __name__ == "__main__":
    main()