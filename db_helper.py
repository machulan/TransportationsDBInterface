import pymssql
from resourses.constants import *


def get_connection():
    # return pymssql.connect(**CONNECTION_DATA)
    return pymssql.connect(server=CONNECTION_DATA['server'],
                           port=CONNECTION_DATA['port'],
                           user=CONNECTION_DATA['user'],
                           password=CONNECTION_DATA['password'],
                           database=CONNECTION_DATA['database'])


def get_str_date(date):
    # print(get_str_date((5, 45, 7)))
    return '.'.join(map(str, date))


def get_report_names():
    # conn = pymssql.connect(server="PC", port=1433, user="sa", password="123456789", database="Transportations")
    # conn = get_connection()
    conn = pymssql.connect(**CONNECTION_DATA)

    cursor = conn.cursor()
    cursor.execute("SELECT so.name FROM sys.objects so WHERE type='P'")

    # result = []
    result = cursor.fetchall()
    result = list(map(lambda item: item[0], result))
    result = list(filter(lambda name: name[:3] != 'sp_', result))
    # result = [(lambda item: item[0])(item) for item in result]
    # row = cursor.fetchone()
    conn.close()
    return result


def get_number_of_kilometers_traveled(driver_id):
    """процедура подсчета количества километров в пути (DriverID, Result OUTPUT)"""
    conn = pymssql.connect(**CONNECTION_DATA)
    cursor = conn.cursor()
    cursor.execute("""
        DECLARE @Number FLOAT
        DECLARE @ReturnStatus INT
        EXECUTE @ReturnStatus = NumberOfKilometersTraveled """ + str(driver_id) + """, @Result = @Number OUTPUT;
        PRINT @Number;

        SELECT @Number;
                """)
    result = cursor.fetchall()[0][0]
    conn.close()
    return result


def get_driver_path_lengths():
    """процедура, возвращающая множество четверок
    'id водителя, имя водителя, фамилия водителя, количество проезженных километров'(DriversCursor OUTPUT)"""
    conn = pymssql.connect(**CONNECTION_DATA)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE #Result (driver_id bigint, first_name nvarchar(255), last_name nvarchar(255), num FLOAT)

        DECLARE @ResultCursor CURSOR;
        EXECUTE GetDriverPathLengthPairs @DriversCursor = @ResultCursor OUTPUT;
        DECLARE @driver_id bigint, @first_name nvarchar(255), @last_name nvarchar(255), @num FLOAT
        FETCH NEXT FROM @ResultCursor INTO @driver_id, @first_name, @last_name, @num
        WHILE(@@FETCH_STATUS = 0)
        BEGIN
            INSERT #Result
                (driver_id, first_name, last_name, num)
            VALUES
                (@driver_id, @first_name, @last_name, @num)
            FETCH NEXT FROM @ResultCursor INTO @driver_id, @first_name, @last_name, @num
        END
        CLOSE @ResultCursor;
        DEALLOCATE @ResultCursor;

        SELECT *
        FROM #Result;
        """)

    # DROP TABLE  # Result;
    result = cursor.fetchall()
    conn.close()
    return result


def get_profit_on_period(begin=(0, 0, 0), end=(0, 0, 0)):
    """процедура расчета прибыли за заданный период(begin, end, Result OUTPUT)"""
    conn = pymssql.connect(**CONNECTION_DATA)
    cursor = conn.cursor()
    cursor.execute("""
        DECLARE @SumProfit FLOAT
        DECLARE @ReturnStatus INT
        DECLARE @Begin DATE = CONVERT(date, '""" + get_str_date(begin) + """', 104)
        DECLARE @End DATE = CONVERT(date, '""" + get_str_date(end) + """', 104)

        EXECUTE @ReturnStatus = GetProfitOnPeriod @Begin, @End, @Result = @SumProfit OUTPUT;

        SELECT @SumProfit;
        """)

    result = cursor.fetchone()[0]
    conn.close()
    return result


def count_costs_on_company_development(begin=(0, 0, 0), end=(0, 0, 0)):
    """процедура расчета затрат на развитие предприятия за период(begin, end, Cost OUTPUT)"""
    conn = pymssql.connect(**CONNECTION_DATA)
    cursor = conn.cursor()
    cursor.execute("""
        DECLARE @CostOnCompanyDevelopment FLOAT;
        DECLARE @Begin DATE = CONVERT(date,'""" + get_str_date(begin) + """',104);
        DECLARE @End DATE = CONVERT(date,'""" + get_str_date(end) + """',104);

        EXECUTE CountCostOnCompanyDevelopment @Begin, @End, @Cost = @CostOnCompanyDevelopment OUTPUT;
        SELECT @CostOnCompanyDevelopment;
        """)

    result = cursor.fetchone()[0]
    conn.close()
    return result


def year_profit_statistics():
    """статистика доходов предприятия по годам за все время(ResultCursor OUTPUT)"""
    conn = pymssql.connect(**CONNECTION_DATA)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE #Result (year_ BIGINT, profit FLOAT, absolute_growth BIGINT, relative_growth FLOAT);

        DECLARE @YearProfitStatisticsCursor CURSOR;
        EXECUTE YearProfitStatistics @ResultCursor = @YearProfitStatisticsCursor OUTPUT;
        DECLARE @year BIGINT, @profit FLOAT, @prev_profit FLOAT = 0
        FETCH NEXT FROM @YearProfitStatisticsCursor INTO @year, @profit
        WHILE (@@FETCH_STATUS = 0)
        BEGIN
            INSERT #Result
                (year_, profit, absolute_growth, relative_growth)
            VALUES
                (@year, @profit, @profit - @prev_profit,
                    IIF(@prev_profit = 0, 100, (@profit - @prev_profit) / @prev_profit * 100))

            SET @prev_profit = @profit
            FETCH NEXT FROM @YearProfitStatisticsCursor INTO @year, @profit
        END
        CLOSE @YearProfitStatisticsCursor
        DEALLOCATE @YearProfitStatisticsCursor;

        SELECT *
        FROM #Result;
        """)

    result = cursor.fetchall()
    conn.close()
    return result





    # cursor.execute("SELECT @@VERSION")
    # print(cursor.fetchone()[0])
    # cursor.execute("SELECT * FROM CSVTest")
    # rr = cursor.fetchall()


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

def test():
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
    # test()
    # exit()

    import shelve
    from login import Account

    admin = Account('Мачула Никита', 'admin', 'admin', 'admin')
    db = shelve.open('accounts')
    db.clear()
    db['admin'] = admin
    print(admin, 'успешно добавлен в базу данных аккаунтов')

    user = Account('Страхов Артем', 'user', 'user', 'user')
    db['user'] = user
    print(user, 'успешно добавлен в базу данных аккаунтов')

    test_user = Account('Гаджик', 'TestUser', '123456789', 'user')
    # db = shelve.open('accounts')
    db['TestUser'] = test_user
    print(test_user, 'успешно добавлен в базу данных аккаунтов')
