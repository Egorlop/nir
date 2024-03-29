from flask import Flask, render_template, request
import psycopg2
import os.path
import os
import multiprocessing
from werkzeug.utils import secure_filename
from database_func.database import findtypes,datetime,coordsandnames,query,deletetables,infoaboutfields,createtables,createnamestable,droptables
from database_func import nir
from database_func.parsing import test
import time

def get_api():
    desc, names1, names2 = test.main()
    app = Flask(__name__)
    UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    connection = psycopg2.connect(
        user='postgres', password='qwerty', host='localhost', port='5433', database='NIR'
    )
    # connection = psycopg2.connect(
    #     user='tudblunfvemyop', password='3500c1988c90cd7ecf44e57c5468def04053e37d10e4c64698165c51f6e3e60b', host='ec2-52-19-170-215.eu-west-1.compute.amazonaws.com', port='5432', database='dbp32ou9fqe7nn'
    # )
    connection.autocommit = True

    # createtables.createtables(connection)
    # createnamestable.createnamestable(connection, names1, names2)

    @app.route('/', methods=['POST', 'GET'])

    def find_fields():
        types = findtypes.findtypes(connection)
        coords, st_names,stats,fields_names = coordsandnames.coordsandnames(connection)
        if request.method == 'POST':
            stat = request.form['station']
            period1, period2 = datetime.date(request.form['period1'], request.form['period2'] )
            att = request.form['att']
            names=list(set(att.split(',')))
            names.sort()
            info, truecount, falsecount,params = query.query(connection,names,stat,period1,period2)
            return render_template('index.html',info=info,station=stat, stations=stats,names=names,fields_names=fields_names, falsecount=falsecount, truecount=truecount,types=types,coords=coords,st_names=st_names,params=params)
        else:
            return render_template('index.html',info=[],station='',stations=stats,names=[],fields_names=fields_names, falsecount=0, truecount=0,types=types,coords=coords,st_names=st_names,params=[0,0,0,0])

    @app.route('/add', methods=['POST', 'GET'])

    def parser():
        data=[]
        mes1=''
        mes3=''
        end, start, stats = infoaboutfields.infoaboutfields(connection)
        dif=end-start
        files_names=[]
        if dif>0:
            mes2='Данные ввводятся в бд'
        else:
            mes2 = 'Данные не вводятся'
        if request.method == 'POST':
            if request.form.get('button1') == 'button1':
                deletetables.deletetables(connection)
                end, start, stats = infoaboutfields.infoaboutfields(connection)
                mes1='Данные успешно удалены '
            elif request.form.get('button2') == 'button2':
                droptables.droptables(connection)
                createtables.createtables(connection)
                createnamestable.createnamestable(connection, names1, names2)
                end, start, stats = infoaboutfields.infoaboutfields(connection)
                mes1 = 'БД создана заново '
            else:
                file = request.files['file']
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open(app.config['UPLOAD_FOLDER']+'/'+filename, 'rb') as f:
                    file_content = f.read()
                with open(app.config['UPLOAD_FOLDER']+'/database_func/parsing/files.txt', 'r') as file:
                    files = file.read()
                files_names=files.split("\n")
                with open(app.config['UPLOAD_FOLDER']+'/database_func/parsing/files.txt', "a+") as file:
                    if filename not in files_names:
                        file.write(filename+"\n")
                        for i in file_content:
                            if len(hex(i)[2:]) == 2:
                                data.append(hex(i)[2:])
                            elif len(hex(i)[2:]) == 1:
                                data.append('0' + hex(i)[2:])
                        nir.main(data[0:7000],connection)
                        mes2 = 'Данные введены в БД'
                    else:
                        mes3='Данный файл уже есть в БД'
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                end, start, stats = infoaboutfields.infoaboutfields(connection)
        return render_template("add.html",mes1=mes1, mes2=mes2, mes3=mes3,stats=stats,end=end,files=files_names)
    return app

def process_one():
    api=get_api()
    api.run()

def process_two():
    while 1:
        print(234)
        time.sleep(3)


if __name__ == '__main__':
    print(123)
    p1 = multiprocessing.Process(target=process_one)
    p2 = multiprocessing.Process(target=process_two)
    p1.start()
    p2.start()




