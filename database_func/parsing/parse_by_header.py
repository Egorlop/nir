from database_func.parsing import parsing_func, ru_station
from database_func.database import addfield, addstation, findstations

def parse(header,header_message_payload, desc,connection):
    day = 1
    if header['type'] == 1:
        mass = parsing_func.parse_mes_template(header_message_payload, desc, header['type'])
        stations, coordinates = findstations.findstations(connection)
        mass['НАИМЕНСТ'] = ru_station.ru_station(mass['НАИМЕНСТ'])
        st_name = ''
        for i in mass['НАИМЕНСТ']:
            if i == ' ':
                break
            else:
                st_name += i
        # mass['НАИМЕНСТ'] = translit(st_name, language_code='ru', reversed=True)
        # mass['НАИМЕНСТ']=mass['НАИМЕНСТ'].replace("'",'`')
        mass['НАИМЕНСТ'] = st_name
        if mass['НАИМЕНСТ'] not in stations or str(mass['КООРДНОМ']) not in coordinates:
            print('stat added')
            addstation.addstation(connection, mass['КООРДНОМ'], mass['НАИМЕНСТ'], header['station'][0:3],
                                  header['station'][3:6])
        for i in mass:
            addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
    if header['type'] in [2, 6, 7, 10, 11]:
        mass = parsing_func.parse_mes_template(header_message_payload, desc, header['type'])
        if header['type'] in [2]:
            day = mass['ДЕНЬ    ']
            for i in mass:
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [6]:
            for i in mass:
                if 'СНЕГПДПР' in i or 'СНЕГЛДПР' in i or 'СНЕГБДПР' in i:
                    day = mass[i]
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [7]:
            day = mass['ОСАДЧИСР']
            for i in mass:
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [10, 11]:
            for i in mass:
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)

    if header['type'] in [3, 4, 5, 8, 9, 12]:
        mass = parsing_func.parse_mes_without_template(header_message_payload, header['type'])
        if header['type'] in [3]:
            day = mass['ДЕНЬ    ']
            for i in mass:
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [4]:
            for i in mass:
                if 'СОЛСПРСТ' in i:
                    if i[-2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        day = int(i[-2] + i[-1])
                    else:
                        day = int(i[-1])
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [5]:
            for i in mass:
                if 'ТЕВМАКТГ' in i or 'ВЛОМАКГГ' in i:
                    if i[-2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        day = int(i[-2] + i[-1])
                    else:
                        day = int(i[-1])
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [8]:
            for i in mass:
                if 'ОБДНЧИСР' in i:
                    day = mass[i]
                if 'ООЯЧИСЛН' in i:
                    day = mass[i]
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [9]:
            day = mass['ДЕНЬ']
            for i in mass:
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
        if header['type'] in [12]:
            for i in mass:
                if 'ДЕНЬ' in i:
                    day = mass[i]
                addfield.addfield(connection, header['station'], i, mass[i], header['year'], header['month'], day)
    return mass