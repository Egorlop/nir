def parse_mes_4(data):
    offset = 0
    mass = {}
    names = {}
    mass['СЧДНЕЙ'] = int(data[offset], 16)
    offset += 1
    for i in range(mass['СЧДНЕЙ']):
        if len(data) > offset + 1:
            mass['СОЛСПРСТ' + str(i + 1)] = int(data[offset]+data[offset + 1], 16)
            offset += 2
            mass['(СОЛСПРСТ)' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            mass['СОЛСПЧАС' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            mass['(СОЛСПЧАС)' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            for k in range(24):
                mass['СОЛСПРУГ' + str(i+1)+str(k + 1)] = int(data[offset], 16)
                offset += 1
                mass['(СОЛСПРУГ)' + str(i+1)+ str(k + 1)] = int(data[offset], 16)
                offset += 1
        else:
            break
    print(offset)
    return mass,names