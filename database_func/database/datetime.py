def date(period1,period2):
    months={
        'January': '1',
        'February': '2',
        'March': '3',
        'April':'4',
        'May': '5',
        'June': '6',
        'July': '7',
        'August': '8',
        'September': '9',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    for i in months:
        if i in period1:
            period1=period1.replace(i,months[i])
    year=period1[-4:]
    day=period1[period1.find(',')-2:period1.find(',')]
    if day[0]==' ':
        day=day.replace(' ','0')
    month=period1[0:2]
    if month[1]==' ':
        month=month.replace(' ',month[0])
        month = month.replace(month[0], '0',1)
    period1=year+'-'+month+'-'+day


    for i in months:
        if i in period2:
            period2=period2.replace(i,months[i])

    year=period2[-4:]
    day=period2[period2.find(',')-2:period2.find(',')]
    if day[0]==' ':
        day=day.replace(' ','0')
    month=period2[0:2]
    if month[1]==' ':
        month=month.replace(' ',month[0])
        month = month.replace(month[0], '0',1)
    period2 = year + '-' + month + '-' + day
    return period1,period2