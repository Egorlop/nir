import time

def infoaboutfields(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT COUNT(*) FROM Fields"""
        )
        start=cursor.fetchone()
        time.sleep(1)
        cursor.execute(
            f"""SELECT COUNT(*) FROM Fields"""
        )
        end=cursor.fetchone()
        cursor.execute(
            f"""SELECT COUNT(*) FROM Stations"""
        )
        stats=cursor.fetchone()
    return end[0],start[0],stats[0]