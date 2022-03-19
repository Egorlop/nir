def parse_mes_3(data):
    offset = 0
    mass = {}
    names = {}
    mass['ДЕНЬ    '] = int(data[offset], 16)
    offset += 1
    mass['СЧГРЕ    '] = int(data[offset], 16)
    offset += 1
    mass['СЧГРОГ   '] = int(data[offset], 16)
    offset += 1
    for i in range(5):
        mass['ТЕЕПОООМ' + str(i + 1)] = int(data[offset] + data[offset + 1], 16)
        offset += 2
        mass['(ТЕЕПОООМ)' + str(i + 1)] = int(data[offset], 16)
        offset += 1
    mass['СНЕПВЫСТ'] = int(data[offset] + data[offset + 1], 16)
    offset += 2
    mass['(СНЕПВЫСТ)'] = int(data[offset], 16)
    offset += 1
    for i in range(8):
        if len(data) > offset + 1:
            mass['СРОКНАБЛ' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            for k in range(6):
                if len(data) > offset + 1:
                    mass['ТЕППЕСТП' + str(i + 1)+str(k + 1)] = int(data[offset] + data[offset + 1], 16)
                    offset += 2
                    mass['(ТЕППЕСТП)' + str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                else:
                    break
        else:
            break
    if len(data) > offset + 1:
        for i in range(8):
            mass['СРОКНАБЛ' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            for k in range(4):
                mass['ТЕОПОООМ'+ str(i + 1) + str(k + 1)] = int(data[offset] + data[offset + 1], 16)
                offset += 2
                mass['(ТЕОПОООМ)'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                offset += 1
    return mass,names