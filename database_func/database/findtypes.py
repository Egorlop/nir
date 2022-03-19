def findtypes(connection):
    names=[]
    for i in range(1,13):
        buf=[]
        with connection.cursor() as cursor:
            type=str(i)
            query = f"SELECT short_name FROM names WHERE type ='{type}' ORDER BY short_name ASC"
            cursor.execute(query)
            cort=cursor.fetchall()
            for i in cort:
                buf.append(i[0])
            buf=list(set(buf))
            names.append(buf)
        for i in names:
            i.sort()
    return names
