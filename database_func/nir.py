from database_func.parsing import test, parsing_func, readfiles,nameses,ru_station,parse_by_header
from database_func.database import addfield, addstation, findstations,createtables, searchstation, createnamestable, deletetables
import psycopg2
import requests

desc,names1,names2= test.main()
def main(data):
    count=1
    offset = 0
    connection = psycopg2.connect(
        user='postgres', password='qwerty', host='localhost', port='5433', database='NIR'
    )
    connection.autocommit = True
    #deletetables.deletetables(connection)
    #createtables.createtables(connection)
    #createnamestable.createnamestable(connection,names1,names2)
    while offset < (len(data)):
        header,offset = parsing_func.parse_header(offset,data)
        header_message_payload = data[offset:offset+header['msg_len']]
        mass=parse_by_header.parse(header,header_message_payload, desc,connection)
        offset = offset + header['msg_len']
        print('#' + str(count) + ".", header)
        print('data:', header_message_payload)
        print('after parse:', mass)
        print('offset:', offset, len(data), '\n')
        count+=1
    connection.close()
    print('[INFO] Connection closed2')
    #12671011

