from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pickle
import os


app = Flask(__name__)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ngoccuong1812'
app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def welcome():
  return redirect('/login')

@app.route("/login", methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    # Request.form: đọc từ file html form box username, pass 
    if request.form['username'] != 'phamcuong' or request.form['password'] != '123':
      error = 'Sai ID hoac mat khau.'
    else:
      return redirect(url_for('accept'))
  return render_template('login.html', error=error)

@app.route('/accept', methods= ['GET','POST'])
def accept():
  cursor= mysql.connect().cursor()
  cursor.execute("SELECT * FROM realtime")
  myresult = cursor.fetchall()
  cursor.close()
  time = []
  day = []
  bienso=[]
  for i in range(len(myresult)):
    time.append(myresult[i][0])
    day.append(myresult[i][1])
    bienso.append(myresult[i][2])
  print(".......")
  print(time)
  print(day)
  print(bienso)
  len_n = len(time)
  if request.method == 'POST':
    if request.form['submit_button'] == 'data':
      return redirect(url_for("data"))
  return render_template('index.html', time= time, day= day, bienso= bienso, len_n=len_n)

@app.route('/data')
def data():
  cursor= mysql.connect().cursor()
  cursor.execute("SELECT * FROM data")
  myresult = cursor.fetchall()
  cursor.close()
  time = []
  day = []
  bienso=[]
  status= []
  for i in range(len(myresult)):
    time.append(myresult[i][0])
    day.append(myresult[i][1])
    bienso.append(myresult[i][2])
    status.append(myresult[i][3])
  print(".......")
  print(time)
  print(day)
  print(bienso)
  print(status)
  len_n = len(time)
  return render_template('data.html', time= time, day= day, bienso= bienso, status= status, len_n= len_n)

if __name__ == '__main__':
    app.run(debug= True)