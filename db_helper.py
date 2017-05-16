# import pyodbc
#
# drs = pyodbc.drivers()
#
# for dr in drs:
#     print(dr)
#
# # Specifying the ODBC driver, server name, database, etc. directly
#
# cnxn = pyodbc.connect(
#     r'DRIVER={SQL Server};'
#     r'SERVER=pc\User;'
#     r'DATABASE=Sandbox;'
#     r'UID=sa;'
#     r'PWD=123456789'
# )
#
# cursor = cnxn.cursor()



# from os import getenv
# PSMODULEPATH

# import os
# for k, v in os.environ.items():
#     if k == 'PATH':
#         for s in v.split(';'):
#             print(s)

# server = getenv("sqlserver")
# user = getenv("sa")
# password = getenv("123456789")

import pymssql

conn = pymssql.connect(server="PC", port=1433, user="sa", password="123456789", database="Sandbox")

cursor = conn.cursor()
# cursor.execute("SELECT @@VERSION")
# print(cursor.fetchone()[0])
cursor.execute("SELECT * FROM CSVTest")
rr = cursor.fetchall()
# row = cursor.fetchone()
# while row:
while False:
    print("ID : {0}, First Name : {1}, Last Name : {2}, Birth Date : {3}".format(*row))
    row = cursor.fetchone()

persons = []
cursor.execute("SELECT * FROM CSVTest")
row = cursor.fetchone()
while row:
    persons.append(row)
    row = cursor.fetchone()

from pymssql import datetime as dt

print(pymssql.Date(2019, 12, 7))
print(pymssql.Time(7, 8, 39))

# persons.extend([(5, 'Иван', 'Иванов', dt.datetime(1900, 1, 3, 7, 8, 39, 0)),
#                (6, 'Сергей', 'Иванов', '1900-01-03 07:10:59')])
# cursor.executemany(
#     '''INSERT CSVTest
#             (ID, FirstName, LastName, BirthDate)
#         VALUES
#             (%d, %s, %s, %s)''', persons)
# conn.commit()

if __name__ == '__main__':
    import shelve
    from login import Account
    admin = Account('admin', 'admin', 'admin')
    db = shelve.open('accounts')
    db.clear()
    db['admin'] = admin

    test_user = Account('TestUser', 'TestUser', '123456789', 'user')
    # db = shelve.open('accounts')
    db['TestUser'] = test_user