import psycopg2

try:
    connection = psycopg2.connect(
        user='postgres', password='qwerty', host='localhost', port='5433',database = 'NIR'
    )
    connection.autocommit = True
    print(connection)
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        print(f'Server version: {cursor.fetchone()}')

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''CREATE TABLE Stations(
    #         id serial PRIMARY KEY,
    #         coordinates integer,
    #         st_name varchar(30),
    #         long smallserial,
    #         width smallserial);
    #         '''
    #     )
    #     print('Table1 created')
    with connection.cursor() as cursor:
        data = "AJaH                 "
        query = f"SELECT id FROM Stations WHERE st_name='{data}'"
        cursor.execute(query)
        res = cursor.fetchone()
        print(res[0])
except Exception as _ex:
    print('[INFO] Error: ', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] Connection closed')
