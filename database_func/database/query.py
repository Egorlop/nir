def query(connection,names,stat,period1,period2):
    info = []
    truecount = []
    falsecount = []
    params=[]
    for k in names:
        k = k.replace(' ', '')
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT * FROM Fields
                WHERE Station in (SELECT id FROM Stations WHERE st_name = '{stat}') and values = 'True'
                and name = '{k}' and date BETWEEN '{period1}' and '{period2}'"""
            )
            info.append(cursor.fetchall())
            cursor.execute(
                f"""SELECT COUNT(*) FROM Fields
                WHERE Station in (SELECT id FROM Stations WHERE st_name = '{stat}') and values = 'True'
                and name = '{k}' and date BETWEEN '{period1}' and '{period2}'"""
            )
            truecount.append(cursor.fetchone())
            cursor.execute(
                f"""SELECT COUNT(*) FROM Fields
                WHERE Station in (SELECT id FROM Stations WHERE st_name = '{stat}') and values = 'False'
                and name = '{k}' and date BETWEEN '{period1}' and '{period2}'"""
            )
            falsecount.append(cursor.fetchone())
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT COUNT(*) FROM Fields"""
        )
        all=cursor.fetchone()[0]
        cursor.execute(
            f"""SELECT COUNT(*) FROM Fields WHERE values = 'True'"""
        )
        true=cursor.fetchone()[0]
        cursor.execute(
            f"""SELECT COUNT(*) FROM Fields WHERE values = 'False'"""
        )
        false=cursor.fetchone()[0]
        params.append(all)
        params.append(true)
        params.append(false)
        params.append((round((true/all),5))*100)
        print(params)
    return info,truecount,falsecount,params