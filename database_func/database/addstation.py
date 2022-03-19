

def addstation(connection, coordinates,st_name,long,width):
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO Stations(coordinates, st_name,long,width) VALUES (%s, %s, %s,%s);"
            data = (coordinates,st_name,long,width)
            cursor.execute(query, data)
            print('Station added')
    except Exception as _ex:
        print('[INFO] Error: ', _ex)