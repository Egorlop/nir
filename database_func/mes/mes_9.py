def parse_mes_9(data):
    offset = 0
    mass = {}
    names = {}
    mass['ДЕНЬ'] = int(data[offset], 16)
    offset += 1
    mass['СЧСРОК'] = int(data[offset], 16)
    offset += 1
    for i in range(1):
        if len(data) > offset+1:
            mass['СРОКНАБЛ' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            mass['СЧАЯ' + str(i + 1)] = int(data[offset], 16)
            offset += 1
            for k in range(20):
                if len(data) > offset + 11:
                    mass['АЯВЛВИД'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                    mass['(АЯВЛВИД)'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                    mass['АЯИНТЕНС'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                    mass['(АЯИНТЕНС)'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                    mass['АЯВРЕМЯН'+ str(i + 1) + str(k + 1)] = int(data[offset]+data[offset+1], 16)
                    offset += 2
                    mass['(АЯВРЕМЯН)'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                    mass['АЯВРЕМЯК'+ str(i + 1) + str(k + 1)] = int(data[offset]+data[offset+1], 16)
                    offset += 2
                    mass['(АЯВРЕМЯК)Q'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                    mass['(АЯВРЕМЯК)'+ str(i + 1) + str(k + 1)] = int(data[offset], 16)
                    offset += 1
                else:
                    break
        else:
            break
    return mass,names