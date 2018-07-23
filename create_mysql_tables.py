from python_mysql_dbconfig import read_db_config
import pymysql
def create_database():
    query = 'create database {}'
    dbconfig = read_db_config()
    try:
        conn = pymysql.connect(user=dbconfig['user'], password=dbconfig['password'])
        cursor = conn.cursor()
        name = ''
        table = ''
        name = input('Enter database name: ')
        table = name
        while(True):
            f = 0
            try:
                cursor.execute(query.format(table))
                f = 1
            except Exception as e:
                print('query', query.format(table))
                print(e)
            finally:
                if f != 1:
                    name = input('Enter other database name or press 1 to continue: ')
                    if name == '1':
                        break
                    table = name
                else:
                    break
        q = 'use {}'.format(table)
        cursor.execute(q)

    except Exception as e:
        print('############################################################\n')
        print(e)
        print('\n')

    finally:
        cursor.close()
        conn.close()
        return table

def insert_remaining_columns(database, tablename, column, values):
    query = 'desc {}'.format(tablename)
    dbconfig = read_db_config()
    res = []
    try:
        conn = pymysql.connect(user=dbconfig['user'], password=dbconfig['password'], database=database)

        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        res = [row[0] for row in rows]

        for ind, col in enumerate(column, 0):
            if col not in res:
                vv = ''
                val = values[ind]
                if type(val) is str:
                    vv = 'varchar(500)'
                elif type(val) is int:
                    vv += 'int(18)'
                elif type(val) is float:
                    vv += 'decimal(19, 6)'
                else:
                    vv += 'boolean'
                q = 'alter table {} add column {} {}'.format(tablename, col, vv)
                cursor.execute(q)

    except Exception as e:
        print('############################################################\n')
        print(e)
        print('\n')

    finally:
        cursor.close()
        conn.commit()
        conn.close()
        return res



def execute_query(database, query, tt = 0):
    dbconfig = read_db_config()
    try:
        conn = pymysql.connect(database=database, user=dbconfig['user'], password=dbconfig['password'])
        cursor = conn.cursor()
        cursor.execute(query)

    except Exception as e:
        # print('*----------------------------------------------------------*')
        # print(query)
        if tt != 0:
            print('############################################################\n')
            print(e)
            print('\n')

    finally:
        cursor.close()
        conn.commit()
        conn.close()
