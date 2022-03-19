
from database_func.mes import mes_9, mes_12, mes_4, mes_3, mes_5, mes_8

def text(data,offset,count):
    text=''
    count1=0
    for i in range(int(count)):
        if offset+i < len(data):
            text=text+data[offset+i]
        else:
            text='0'
            break
    return text

def parse_header(offset, data):
    new_offset= offset + 12
    return {
        'msg_len': int(data[offset]+data[offset+1],16)-12,
        'year': int(data[offset+4]+data[offset+5],16),
        'month': int(data[offset+6],16),
        'station': str(int(data[offset+7]+data[offset+8]+data[offset+9]+data[offset+10],16)),
        'type': int(data[offset+11],16)
    },new_offset

def parse_a_type(data):
    station = ''
    for i in data:
        station = station + i
    dkoistation = ''
    for i in range(0, len(station), 2):
        if station[i] + station[i + 1] in dkoi:
            dkoistation = dkoistation + dkoi[station[i] + station[i + 1]]
        else:
            dkoistation = station[i] + station[i + 1]


    return dkoistation
def parse_mes_template(data, desc,type):
    mass = {}
    offset=0
    for i in desc[type]:
        if desc[type][i][0]=='GRP' or desc[type][i][0]=='GRV':
            count = {}
            buf=1
            keys_list=list(desc[type][i][1].keys())
            for k in range(int(desc[type][i][2])):
                for d in keys_list:
                    if offset < len(data):
                        if desc[type][i][1][d][1] == 'B':
                            mass[d+str(buf)]=int(text(data, offset, desc[type][i][1][d][2]),16)
                        else:
                            mass[d+str(buf)]=parse_a_type(data[offset:offset+int(desc[type][i][1][d][2])])
                    else:
                        break
                    offset = offset + int(desc[type][i][1][d][2])
                buf+=1
        else:
            if desc[type][i][1]=='A':
                mass[i]=parse_a_type(data[offset:offset+int(desc[type][i][2])])
                offset = offset + int(desc[type][i][2])
            else:
                mass[i]=int(text(data,offset,desc[type][i][2]),16)
                offset=offset+int(desc[type][i][2])
    return mass

def parse_mes_without_template(data, type):
    mass={}
    if type == 3:
        mass,names = mes_3.parse_mes_3(data)
    elif type == 4:
        mass,names = mes_4.parse_mes_4(data)
    elif type == 5:
        mass,names = mes_5.parse_mes_5(data)
    elif type == 8:
        mass,names = mes_8.parse_mes_8(data)
    elif type == 9:
        mass,names = mes_9.parse_mes_9(data)
    elif type == 12:
        mass,names = mes_12.parse_mes_12(data)
    return mass

dkoi={
    '4b': '.', '4d': '(', '5d':')','60':'-','61':'/', '6b': '-', '00': 'NULL', '0f':'SI', '40': ' ', '7a': ':','b7':'ъ',
    'b8': 'Ю', 'b9': 'А', 'ba': 'Б', 'bb': 'Ц', 'bc': 'Д', 'bd': 'Е', 'be': 'Ф', 'bf': 'Г',
    'c0': '{' , 'c1': 'A', 'c2': 'B', 'c3': 'C', 'c4': 'D', 'c5': 'E', 'c6': 'F', 'c7': 'G',
    'c8': 'H' , 'c9': 'I', 'ca': 'Х', 'cb': 'И', 'cc': 'Й', 'cd': 'К', 'ce': 'Л', 'cf': 'М',
    'd0': '}' , 'd1': 'J', 'd2': 'K', 'd3': 'L', 'd4': 'M', 'd5': 'N', 'd6': 'O', 'd7': 'P',
    'd8': 'Q' , 'd9': 'R', 'da': 'Н', 'db': 'О', 'dc': 'П', 'dd': 'Я', 'de': 'Р', 'df': 'С',
    'e0': '', 'e1': '', 'e2': 'S', 'e3': 'T', 'e4': 'U', 'e5': 'V', 'e6': 'W', 'e7': 'X',
    'e8': 'Y', 'e9': 'Z', 'ea': 'Т', 'eb': 'У', 'ec': 'Ж', 'ed': 'В', 'ee': 'Ь', 'ef': 'Ы',
    'f0': '0', 'f1': '1', 'f2': '2', 'f3': '3', 'f4': '4', 'f5': '5', 'f6': '6', 'f7': '7',
    'f8': '8', 'f9': '9', 'fa': 'З', 'fb': 'Ш', 'fc': 'Э', 'fd': 'Щ', 'fe': 'Ч', 'ff': 'EO',
}