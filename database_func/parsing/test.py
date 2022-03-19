from database_func.parsing import nameses

def parseGRP1(dict):
    data = {}
    off=0
    while off<len(dict):
        i = dict[off]
        if 'MIT' in i:
            data[i[i.find('T')+2:i.find('T')+12]] = ['MIT', i[i.find('(')-1],i[i.find('(')+1],i[i.find('//')+2:i.find('\n')]+i[i.find('\n')]]
        if 'CHA' in i:
            if i[i.find(')')+2]=='Q' and i[i.find(')')+3]==' ':
                data[i[i.find('A') + 1:i.find('A') + 11]+'Q'] = ['CHA', 'B', i[i.find('B') + 2],i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
            else:
                data[i[i.find('A') + 1:i.find('A') + 11]] = ['CHA', 'B', i[i.find('B') + 2],i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
        off+=1
    return {'name': dict[0][dict[0].find('P')+2:dict[0].find(';')],
            'quantity': dict[1][dict[1].find('(')+1:dict[1].find(')')],
            'data':data,
            'translate':dict[0][dict[0].find('//')+2:dict[0].find('\n')]+dict[0][dict[0].find('\n')]}

def parseGRV1(dict,type):
    data = {}
    off=2
    while off<len(dict):
        i = dict[off]
        if 'MIT' in i:
            if type == 11:
                data[i[i.find('T') + 6:i.find('T') + 14]] = ['MIT', i[i.find('(') - 1], i[i.find('(') + 1:i.find(')')],i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
            else:
                data[i[i.find('T')+2:i.find('T')+10]] = ['MIT', i[i.find('(')-1],i[i.find('(')+1:i.find(')')],i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
        if 'CHA' in i:
            data[i[i.find('A') + 1:i.find('A') + 11]] = ['CHA', i[i.find('Q') + 3], i[i.find('Q') + 5],i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
        if 'CNT' in i:
            data[i[i.find('С'):i.find('С')+8]] = ['CNT', 'B', i[i.find('(') + 1],i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
        if 'KEY' in i:
            data[i[i.find(')')+2:i.find(')')+10]] = ['KEY', 'B', 1,i[i.find('//') + 2:i.find('\n')] + i[i.find('\n')]]
        off+=1
    return {'name': dict[0][dict[0].find(')')+2:dict[0].find(';')],
            'quantity': dict[1][dict[1].find('(')+1:dict[1].find(')')],
            'data':data,
            'translate':dict[0][dict[0].find('//')+2:dict[0].find('\n')]+dict[0][dict[0].find('\n')]}

def main():
    with open(r"C:\Users\egorp\OneDrive\Рабочий стол\НИР\Tms.ddl", 'r') as f:
        dict = f.read()
    names = []
    dict1=dict.split('\n')
    dict1 = dict1[9:]
    desc = {i: {} for i in range(1,13)}
    off = 0
    type=0
    while off < len(dict1):
        if 'RBODY' in dict1[off]:
            type = int(dict1[off][dict1[off].find('(')+1:dict1[off].find(')')])
        if type in [1,2,6,7,10,11]:
            if 'MIT' in dict1[off]:
                desc[type][dict1[off][dict1[off].find('T')+2:dict1[off].find('T')+10]] = ['MIT', dict1[off][dict1[off].find('(')-1],dict1[off][dict1[off].find('(')+1:dict1[off].find(')')],dict1[off][dict1[off].find('//')+2:dict1[off].find('\n')]+dict1[off][dict1[off].find('\n')]]
            if 'CHA' in dict1[off]:
                desc[type][dict1[off][dict1[off].find('A')+1:dict1[off].find('A')+12]] = ['CHA', dict1[off][dict1[off].find('Q')+3],dict1[off][dict1[off].find('Q')+5],dict1[off][dict1[off].find('//')+2:dict1[off].find('\n')]+dict1[off][dict1[off].find('\n')]]
            if 'CNT' in dict1[off]:
                desc[type][dict1[off][dict1[off].find('С'):dict1[off].find('С') + 8]] = ['CNT','B',dict1[off][dict1[off].find('(') + 1],dict1[off][dict1[off].find('//')+2:dict1[off].find('\n')]+dict1[off][dict1[off].find('\n')]]
            if 'KEY' in dict1[off]:
                desc[type][dict1[off][dict1[off].find(')')+2:dict1[off].find(')') + 10]] = ['KEY','B',dict1[off][15:][dict1[off][15:].find(')') -1],dict1[off][dict1[off].find('//')+2:dict1[off].find('\n')]+dict1[off][dict1[off].find('\n')]]
            if 'GRP' in dict1[off]:
                i=0
                while 1:
                    if 'END '+dict1[off][dict1[off].find('P')+2:dict1[off].find(';')] in dict1[off+i]:
                        grp = parseGRP1(dict1[off:off+i+1])
                        desc[type][grp['name']] = ['GRP',grp['data'], grp['quantity']]
                        off+=i
                        break
                    else:
                        i+=1
            if 'GRV' in dict1[off] or 'GRK' in dict1[off]:
                i=0
                while 1:
                    if 'END '+dict1[off][dict1[off].find(')')+2:dict1[off].find(';')] in dict1[off+i]:
                        grv = parseGRV1(dict1[off:off + i + 1],type)
                        desc[type][grv['name']] = ['GRV', grv['data'], grv['quantity']]
                        off += i
                        break
                    else:
                        i+=1
        off+=1
    for type in [1,2,6,7,10,11]:
        for i in desc[type]:
            if len(desc[type][i])==4:
                names.append([i,desc[type][i][3],type])
            else:
                for k in desc[type][i][1]:
                    names.append([k,desc[type][i][1][k][3],type])
    new_names= nameses.names()
    return desc,names,new_names

