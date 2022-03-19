
def searchstation(connection):
    try:
        with connection.cursor() as cursor:
            stations = "'BAL                 ','POGIBI              '"
            cursor.execute(
                f"""SELECT * FROM Fields
                WHERE Station in (SELECT id FROM Stations WHERE st_name IN ({stations}))
                LIMIT 5;"""
            )
            res = cursor.fetchall()
            print(res)
            cursor.execute(
                """SELECT * FROM Fields 
                WHERE year BETWEEN 2012 and 2015
                or year BETWEEN 2017 and 2021
                 LIMIT 5;"""
            )
            res = cursor.fetchall()
            print(res)
            cursor.execute(
                """SELECT * FROM Fields
                WHERE Station in (SELECT id FROM Stations WHERE st_name IN ('BAL                 ','POGIBI              '))
                and year BETWEEN 2017 and 2021
                LIMIT 5;"""
            )
            res = cursor.fetchall()
            print(res)
            cursor.execute(
                """SELECT * 
                FROM fields AS F
                JOIN stations AS S 
                ON F.station = S.id
                WHERE s.st_name IN ('BAL                 ','POGIBI              ')
                LIMIT 5;"""
            )
            res = cursor.fetchall()
            print(res)


    except Exception as _ex:
        print('[INFO] Error: ', _ex)