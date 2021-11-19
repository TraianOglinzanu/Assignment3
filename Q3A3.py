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

def smallUniformed():
    global connection
    import time
    db_path = './A3Small2.db'
    connect(db_path)

    cursor.execute(' PRAGMA automatic_index=false')

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT CAST (oi.order_item_id AS REAL)/CAST(COUNT(o.order_id) AS REAL) average FROM Customers c, Orders o, Order_items oi WHERE c.customer_id = o.customer_id  AND o.order_id = oi.order_id AND customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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
        cursor.execute(" SELECT CAST (oi.order_item_id AS REAL)/CAST(COUNT(o.order_id) AS REAL) average FROM Customers c, Orders o, Order_items oi WHERE c.customer_id = o.customer_id  AND o.order_id = oi.order_id AND customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

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

    cursor.execute(' PRAGMA foreign_keys=ON; ')
    cursor.execute(' PRAGMA automatic_index=true')

    cursor.execute("DROP INDEX IF EXISTS a_customer_id_index")
    cursor.execute("DROP INDEX IF EXISTS b_customer_id_index")
    cursor.execute("DROP INDEX IF EXISTS c_customer_id_index")
    cursor.execute("DROP INDEX IF EXISTS d_customer_id_index")

    cursor.execute("CREATE INDEX a_customer_id_index ON Customers(customer_id)")
    cursor.execute("CREATE INDEX b_customer_id_index ON Orders(customer_id)")
    cursor.execute("CREATE INDEX c_customer_id_index ON Order_items(order_id)")
    cursor.execute("CREATE INDEX d_customer_id_index ON Orders(order_id)")

    connection.commit()

    start_time=time.time()

    for i in range(50):
        cursor.execute(" SELECT CAST (oi.order_item_id AS REAL)/CAST(COUNT(o.order_id) AS REAL) average FROM Customers c, Orders o, Order_items oi WHERE c.customer_id = o.customer_id  AND o.order_id = oi.order_id AND customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);" )

    end_time=time.time()
    exec_time =  (end_time - start_time)*1000

    cursor.execute("DROP INDEX IF EXISTS a_customer_id_index")
    cursor.execute("DROP INDEX IF EXISTS b_customer_id_index")
    cursor.execute("DROP INDEX IF EXISTS c_customer_id_index")
    cursor.execute("DROP INDEX IF EXISTS d_customer_id_index")
  
    connection.commit()
    connection.close()

    return exec_time

def mediumUniformed():
    global connection
    import time
    db_path = './A3Medium.db'
    connect(db_path)

    cursor.execute(' PRAGMA foreign_keys=OFF; ')
    cursor.execute(' PRAGMA automatic_index=false')

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

    cursor.execute(' PRAGMA foreign_keys=ON; ')
    cursor.execute(' PRAGMA automatic_index=true')

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
    cursor.execute(' PRAGMA automatic_index=false')

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

    cursor.execute(' PRAGMA foreign_keys=ON; ')
    cursor.execute(' PRAGMA automatic_index=true')

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
    # ax.set_title("Query 3")
    # ax.legend()

    # tl = "Query_3"

    # path = './{}_barchart.png'.format(tl)
    # plt.savefig(path)
    # print('Chart saved to file {}'.format(path))

    # plt.close()
    # return

    print("Small Uninformed: " + str(one))
    print("Small Self-optimized: " + str(two))
    print("Small User-optimized: " + str(three))

    #print("------------------------------------")

    # print("Medium Unoptimized: " + str(four))
    # print("Medium SelfOptimized: " + str(five))
    # print("Medium UserOptimized: " + str(six))

    #print("------------------------------------")

    # print("Large Uninformed: " + str(seven))
    # print("Large Self-optimized: " + str(eight))
    # print("Large User-optimized: " + str(nine))

    return

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
  
if __name__ == "__main__":
    main()