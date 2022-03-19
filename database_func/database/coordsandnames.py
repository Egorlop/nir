def coordsandnames(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT st_name,coordinates FROM Stations ORDER BY st_name ASC"""
        )
        stats = cursor.fetchall()
        cursor.execute(
            f"""SELECT DISTINCT name,long_name FROM fields ORDER BY name ASC"""
        )
        fields_names = cursor.fetchall()
    coords = []
    st_names = []
    for i in stats:
        k=''
        if i[1][2]=='0':
            k=i[1][0:2]+'1'+i[1][3:]
        else:
            k=i[1]
        if k[5]=='0':
            k=i[1][0:5]+'11'
        if k[6]=='1':
            k=k[0:3]+'1'+k[3:]
            coords.append([(int(k[0:3]) / 10), (int(k[3:7])/10)])
        else:
            k = k[0:6] + '1'
            coords.append([(int(k[0:3]) / 10), (int(k[3:7]) / 100)])
        st_names.append(i[0])

    return coords,st_names,stats,fields_names
