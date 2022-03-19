def findstations(connection):
    stations = []
    coordinates = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT st_name,coordinates FROM stations'
            )
            res = cursor.fetchall()
            for i in range(len(res)):
                stations.append(res[i][0])
                coordinates.append(res[i][1])
            print('Stations and coord finded')
            return stations,coordinates
    except Exception as _ex:
        print('[INFO] Error: ', _ex)