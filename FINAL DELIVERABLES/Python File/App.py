from flask import Flask, render_template, flash, request, session
from flask import render_template, redirect, url_for, request
import datetime

import ibm_db
import pandas
import ibm_db_dbi
from sqlalchemy import create_engine

engine = create_engine('sqlite://',
                       echo = False)

dsn_hostname = "b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
dsn_uid = "zht77907"
dsn_pwd = "12CV4yAJK0mxMABC"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_port = "31249"
dsn_protocol = "TCPIP"
dsn_security = "SSL"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)



try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/Home")
def Home():
    return render_template('index.html')
@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')
@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/NewMedicine")
def NewMedicine():
    return render_template('NewMedicines.html')





@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

           conn = ibm_db.connect(dsn, "", "")
           pd_conn = ibm_db_dbi.Connection(conn)
           selectQuery = "SELECT * FROM regtb  "
           dataframe = pandas.read_sql(selectQuery, pd_conn)
           dataframe.to_sql('booktb1', con=engine, if_exists='append')
           data = engine.execute("SELECT * FROM booktb1").fetchall()

           return render_template('AdminHome.html', data=data)

       else:
        return render_template('index.html', error=error)




@app.route("/newmedi", methods=['GET', 'POST'])
def newmedi():
    if request.method == 'POST':


        uname = session['uname']
        dname = request.form['dname']
        mname = request.form['mname']
        tim = request.form['tim']
        qty = request.form['qty']

        info = request.form['info']


        file = request.files['file']
        file.save("static/upload/" + file.filename)


        conn = ibm_db.connect(dsn, "", "")

        insertQuery =  "INSERT INTO meditb VALUES ('"+ uname +"','" + dname + "','" + mname + "','" + tim + "','" + qty + "','" + info + "','" + file.filename + "')"
        insert_table = ibm_db.exec_immediate(conn, insertQuery)


        alert = 'Medicine info saved successfully'
        return render_template('goback.html', data=alert)





@app.route("/MedicineInfo")
def MedicineInfo():



    conn = ibm_db.connect(dsn, "", "")
    pd_conn = ibm_db_dbi.Connection(conn)
    selectQuery = "SELECT * FROM meditb  "
    dataframe = pandas.read_sql(selectQuery, pd_conn)
    dataframe.to_sql('booktb1', con=engine, if_exists='append')
    data = engine.execute("SELECT * FROM booktb1").fetchall()

    return render_template('MedicinesInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']




        conn = ibm_db.connect(dsn, "", "")

        insertQuery = "INSERT INTO regtb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "')"
        insert_table = ibm_db.exec_immediate(conn, insertQuery)
        # return 'file register successfully'


    return render_template('UserLogin.html')










@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']


        conn = ibm_db.connect(dsn, "", "")
        pd_conn = ibm_db_dbi.Connection(conn)

        selectQuery = "SELECT * from regtb where UserName='" + username + "' and password='" + password + "'"
        dataframe = pandas.read_sql(selectQuery, pd_conn)

        if dataframe.empty:
            data1 = 'Username or Password is wrong'
            return render_template('goback.html', data=data1)
        else:
            print("Login")
            selectQuery = "SELECT * from regtb where UserName='" + username + "' and password='" + password + "'"
            dataframe = pandas.read_sql(selectQuery, pd_conn)

            dataframe.to_sql('Employee_Data',
                             con=engine,
                             if_exists='append')

            # run a sql query
            print(engine.execute("SELECT * FROM Employee_Data").fetchall())

            return render_template('UserHome.html', data=engine.execute("SELECT * FROM Employee_Data").fetchall())





@app.route("/UserHome")
def UserHome():

    username = session['uname']


    conn = ibm_db.connect(dsn, "", "")
    pd_conn = ibm_db_dbi.Connection(conn)
    selectQuery = "SELECT * FROM regtb where username='" + username + "'"
    dataframe = pandas.read_sql(selectQuery, pd_conn)
    dataframe.to_sql('booktb1', con=engine, if_exists='append')
    data = engine.execute("SELECT * FROM booktb1").fetchall()

    return render_template('UserHome.html', data=data)


@app.route("/Alert")
def Alert():

    from datetime import datetime
    import pandas as pd
    # Get current time in local timezone
    current_time = datetime.now()
    print('Current timestamp: ', current_time.strftime('%H:%M:%S'))

    dd1 = current_time.strftime('%H:%M:%S')

    n = 15
    # Add 2 minutes to datetime object containing current time
    future_time = current_time + pd.DateOffset(minutes=n)
    print('Future Time (2 minutes from now ): ', future_time)
    # Convert datetime object to string in specific format
    future_time_str = future_time.strftime('%H:%M:%S')
    print('Future Time as string object: ', future_time_str)

    dd2 = future_time_str











    username = session['uname']


    conn = ibm_db.connect(dsn, "", "")
    pd_conn = ibm_db_dbi.Connection(conn)
    selectQuery = "SELECT * FROM meditb  where Time between '"+ dd1 +"' and '"+ dd2+"'"
    dataframe = pandas.read_sql(selectQuery, pd_conn)
    dataframe.to_sql('booktb1', con=engine, if_exists='append')

    data = engine.execute("SELECT * FROM booktb1  ").fetchall()

    for item1 in data:
        uname = item1[1]

        uname =item1[1]
        dname = item1[2]
        mname = item1[3]
        tim =item1[4]
        qty = item1[5]

        from gtts import gTTS

        # This module is imported so that we can
        # play the converted audio
        import os

        # The text that you want to convert to audio
        mytext = 'Medicine Name ' + mname + ' Quantity'+ qty

        # Language in which you want to convert
        language = 'en'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("welcome.mp3")
        os.system("welcome.mp3")


        selectQuery = "SELECT  *  FROM  regtb where Username='" + uname + "'"
        dataframe = pandas.read_sql(selectQuery, pd_conn)

        dataframe.to_sql('regtb', con=engine, if_exists='append')
        data2 = engine.execute("SELECT * FROM regtb").fetchall()

        for item in data2:
            email = item[4]









    return render_template('Alert.html', data=data)

@app.route("/Remove", methods=['GET'])
def Remove():


    unmae = request.args.get('id')
    mname = request.args.get('mname')
    conn = ibm_db.connect(dsn, "", "")
    pd_conn = ibm_db_dbi.Connection(conn)

    insertQuery = "Delete from meditb  where  username='"+ unmae +"' and MediName='"+mname +"'"
    insert_table = ibm_db.exec_immediate(conn, insertQuery)


    selectQuery = "SELECT * from meditb "
    dataframe = pandas.read_sql(selectQuery, pd_conn)

    dataframe.to_sql('Employee_Data',
                     con=engine,
                     if_exists='append')

    # run a sql query
    print(engine.execute("SELECT * FROM Employee_Data").fetchall())

    return render_template('MedicinesInfo.html', data=engine.execute("SELECT * FROM Employee_Data").fetchall())





if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)