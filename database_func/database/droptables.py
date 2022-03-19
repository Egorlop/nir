def droptables(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                'DROP TABLE names'
            )
            cursor.execute(
                'DROP TABLE fields'
            )
            cursor.execute(
                'DROP TABLE stations'
            )
            print('Tables droped')
    except Exception as _ex:
        print('[INFO] Error: ', _ex)