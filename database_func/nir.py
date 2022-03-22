from database_func.parsing import test, parsing_func, parse_by_header
import psycopg2

desc,names1,names2= test.main()
def main(data,connection):
    count=1
    offset = 0
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
        #print('data:', header_message_payload)
        #print('after parse:', mass)
        print('offset:', offset, len(data), '\n')
        count+=1
    print('[INFO] Connection closed2')
    #12671011

