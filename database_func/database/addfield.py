def addfield(connection,station,name,values,year,month,day):
    names = []
    try:
        with connection.cursor() as cursor:
            query = f"SELECT id FROM Stations WHERE coordinates='{station}'"
            cursor.execute(query)
            id = cursor.fetchone()
            if str(values) == '32768':
                value=False
            else:
                value=True

            cursor.execute(
                'SELECT * FROM names'
            )
            res = cursor.fetchall()
            short = ''
            for i in range(len(res)):
                names.append(res[i][1])
            for i in names:
                count = 0
                for k in i:
                    if k == name[count]:
                        count+=1
                    else:
                        break
                if count == len(i):
                    short = i
                    break
            query = f"SELECT long_name FROM names WHERE short_name='{short}'"
            cursor.execute(query)
            long = cursor.fetchone()[0]
            if 'CHA' in long:
                long='NULL'
            for k in range(4):
                if name[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                    name = name[0:-1]
            name=name.replace(' ','')
            if len(str(day))==1:
                day = '0'+str(day)
            if len(str(month))==1:
                month = '0'+str(month)
            date = str(year)+'-'+str(month)+'-'+str(day)
            query = "INSERT INTO Fields(station, name, long_name, values,date) VALUES (%s, %s, %s,%s,%s);"
            data = (id[0], name, long[0:49], value, date)
            cursor.execute(query, data)
    except Exception as _ex:
        print('[INFO]  add: ', _ex,long, name)

