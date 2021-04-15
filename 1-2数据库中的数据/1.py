import pymysql

mydb = pymysql.connect(host="localhost",    # ①
                       user='root',
                       password='1q2w3e4r5t',
                       db="books",
                      )