def readfiles():
    data = []
    with open(r"D:\NIR\parsing\files", 'r') as f:
        files = f.read().split('\n')
    for i in files:
        print(i)
        with open(i, 'rb') as f:
            data1 = f.read()
        for i in data1:
            if len(hex(i)[2:]) == 2:
                data.append(hex(i)[2:])
            elif len(hex(i)[2:]) == 1:
                data.append('0' + hex(i)[2:])
    print(len(data))
    return data