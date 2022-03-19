def deletetables(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                'DELETE FROM fields'
            )
            cursor.execute(
                'DELETE FROM stations'
            )
            print('Tables deleted')
    except Exception as _ex:
        print('[INFO] Error: ', _ex)