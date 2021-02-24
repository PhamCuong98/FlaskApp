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

@app.route('/accept', methods= ['GET'])
def accept():
  cursor= mysql.connect().cursor()
  cursor.execute("SELECT * FROM bienso")
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
  return render_template('index.html', time= time, day= day, bienso= bienso, len_n=len_n)

@app.route("/login", methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'phamcuong' or request.form['password'] != '123':
      error = 'Sai ID hoac mat khau.'
    else:
      return redirect(url_for('accept'))
  return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug= True)