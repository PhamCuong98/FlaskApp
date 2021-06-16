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
      return redirect(url_for('welcomes'))
  return render_template('login.html', error=error)

@app.route('/welcomes', methods = ['GET', 'POST'])
def welcomes():
  if request.method == 'POST':
    print("Vao Post")
    if request.form.get('Live') == 'Live':
      print("Live")
      return redirect(url_for('live'))

    if  request.form.get('Data') == 'Data':
      print("Data")
      return redirect(url_for('data'))
  elif request.method == 'GET':
    print("None")
  return render_template("welcome.html")


@app.route('/live', methods= ['GET','POST'])
def live():
  cursor= mysql.connect().cursor()
  cursor.execute("SELECT * FROM realtime")
  myresult = cursor.fetchall()
  cursor.close()
  time = []
  day = []
  bienso=[]
  Id=[]
  for i in range(len(myresult)):
    time.append(myresult[i][0])
    day.append(myresult[i][1])
    bienso.append(myresult[i][2])
    Id.append(myresult[i][3])
  print(".......")
  print(time, day, bienso)
  len_n = len(time)
  if request.method == 'POST':
    if request.form['submit_button'] == 'Data':
      return redirect(url_for("data"))
  return render_template('index.html', time= time, day= day, bienso= bienso, len_n=len_n, Id= Id)

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
  Id=[]
  for i in range(len(myresult)):
    time.append(myresult[i][0])
    day.append(myresult[i][1])
    bienso.append(myresult[i][2])
    status.append(myresult[i][3])
    Id.append(myresult[i][4])
  print(".......")
  print(time, day, bienso, status)
  len_n = len(time)
  return render_template('data.html', time= time, day= day, bienso= bienso, status= status, len_n= len_n, Id= Id)

if __name__ == '__main__':
    app.run(debug= True)