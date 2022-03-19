def parse_mes_5(data):
    offset = 0
    mass = {}
    names= {}
    mass['СЧГР1'] = int(data[offset], 16)
    offset += 1
    mass['СЧГР2'] = int(data[offset], 16)
    offset += 1
    for i in range(mass['СЧГР1']):
        mass['ТЕВМАКТГ' + str(i + 1)] = int(data[offset]+data[offset + 1], 16)
        offset += 2
        mass['(ТЕВМАКТГ)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['ТЕВМИНТГ' + str(i + 1)] = int(data[offset]+data[offset + 1], 16)
        offset += 2
        mass['(ТЕВМИНТГ)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        for k in range(24):
            mass['ТЕМВОЗТГ' + str(i + 1) + str(k + 1)] = int(data[offset]+data[offset + 1], 16)
            offset += 2
            mass['(ТЕМВОЗТГ)' + str(i + 1) + str(k + 1)] = int(data[offset], 16)
            offset += 1
    for i in range(mass['СЧГР2']):
        mass['ВЛОМАКГГ' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['(ВЛОМАКГГ)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['ВЛОМИНГГ' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        mass['(ВЛОМИНГГ)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
        for k in range(24):
            mass['ВЛОТВЗГГ' + str(i + 1) + str(k + 1)] = int(data[offset], 16)
            offset += 1
            mass['(ВЛОТВЗГГ)' + str(i + 1) + str(k + 1)] = int(data[offset], 16)
            offset += 1
    return mass,names