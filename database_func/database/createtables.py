def createtables(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT version();'
            )
            print(f'Server version: {cursor.fetchone()}')
        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE Names(
                id serial PRIMARY KEY,
                short_name varchar(15),
                long_name varchar(60),
                type varchar(2));
                '''
            )
            print('Table3 created')
        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE Stations(
                id serial PRIMARY KEY,
                coordinates varchar (7),
                st_name varchar(30),
                long smallserial,
                width smallserial);
                '''
            )
            print('Table1 created')

        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE Fields(
                id serial PRIMARY KEY,
                station integer references Stations(id),
                name varchar(15),
                long_name varchar(50),
                values boolean,
                date date);
                '''
            )
            print('Table2 created')

    except Exception as _ex:
        print('[INFO] Error: ', _ex)