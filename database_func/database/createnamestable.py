def createnamestable(connection,names1,names2):
    stations = []
    count=0
    try:
        with connection.cursor() as cursor:
            for i in names2:
                query = "INSERT INTO Names(short_name,long_name,type) VALUES (%s,%s,%s);"
                data = (i,names2[i][0],names2[i][1])
                cursor.execute(query, data)
            for i in names1:
                query = "INSERT INTO Names(short_name,long_name,type) VALUES (%s,%s,%s);"
                data = (i[0],i[1],i[2])
                cursor.execute(query, data)
            return stations
    except Exception as _ex:
        print('[INFO] Error: ', _ex)