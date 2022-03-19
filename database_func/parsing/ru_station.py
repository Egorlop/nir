def ru_station(name):
    if 'E' in name:
        name=name.replace('E','Е')
    if 'T' in name:
        name=name.replace('T','Т')
    if 'O' in name:
        name=name.replace('O','О')
    if 'A' in name:
        name=name.replace('A','А')
    if 'H' in name:
        name=name.replace('H','Н')
    if 'K' in name:
        name=name.replace('K','К')
    if 'X' in name:
        name=name.replace('X','Х')
    if 'M' in name:
        name=name.replace('M','М')
    if 'C' in name:
        name=name.replace('C','С')
    if 'B' in name:
        name=name.replace('B','В')
    if 'C' in name:
        name=name.replace('C','С')
    if 'P' in name:
        name=name.replace('P','Р')
    return name
