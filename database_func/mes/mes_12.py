def parse_mes_12(data):
    offset = 0
    mass = {}
    names ={}
    mass['NZAP'] = int(data[offset], 16)
    offset += 1
    mass['СЧЧАСД'] = int(data[offset]+data[offset+1], 16)
    offset += 2
    for i in range(mass['СЧЧАСД']):
        mass['ДЕНЬ' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['НЧАС' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['МИННАЧ' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['(МИННАЧ)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['МИНКОН' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['(МИНКОН)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        for k in range(6):
            mass['ОСКОЛ' + str(i + 1) + str(k + 1)] = int(data[offset] + data[offset + 1], 16)
            offset += 2
            mass['(ОСКОЛ)' + str(i + 1) + str(k + 1)] = int(data[offset], 16)
            offset += 1
    return mass,names