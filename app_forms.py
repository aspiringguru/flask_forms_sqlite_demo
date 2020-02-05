from flask import Flask, request, flash, url_for, redirect, render_template
from forms import ContactForm
#import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'


#----------nb: below replaces previous creation of database in cr8_SQLite_db.py
db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
       self.name = name
       self.city = city
       self.addr = addr
       self.pin = pin

#----------nb: above replaces previous creation of database in cr8_SQLite_db.py

@app.route('/')
#def home():
#   return render_template('home.html')
def show_all():
   temp = students.query.all()
   print("students.query.all() = ", temp)
   return render_template('show_all.html', students = temp )

@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/new', methods = ['GET', 'POST'])
def new():
   print("@app.route('/new'")
   if request.method == 'POST':
      print("request.method == 'POST'")
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         print("error - Please enter all the fields")
         flash('Please enter all the fields', 'error')
      else:
         print("create students object with form elements.")
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         print("student = ", student)

         db.session.add(student)
         db.session.commit()
         print('Record was successfully added and committed.')
         flash('Record was successfully added and committed.')
         return redirect(url_for('show_all'))
   print("request.method != 'POST', ie GET.")
   return render_template('new.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   print("@app.route('/addrec'")
   if request.method == 'POST':
      print("request.method == 'POST'")
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) \
               VALUES (?,?,?,?)",(nm,addr,city,pin) )
            con.commit()
            msg = "Record successfully added"
            print("Record successfully added")
      except:
         con.rollback()
         msg = "error in insert operation"
         print("error in insert operation")
      finally:
         con.close()
         return render_template("result.html",msg = msg)
   else:
      print("request.method != 'POST'")
      return "request.method != 'POST'"


@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from students")
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   if request.method == 'POST':
      print("@app.route('/contact' > POST")
      if form.validate() == False:
         print("form.validate() == False")
         flash('All fields are required.')
         return render_template('form_contact.html', form = form)
      else:
         print("form.validate() != False")
         name =  request.form["name"]
         print("name=", name)
         Gender =  request.form["Gender"]
         print("Gender=", Gender)
         Address =  request.form["Address"]
         print("Address=", Address)
         return render_template('form_success.html')
   elif request.method == 'GET':
       print("@app.route('/contact' > GET")
       return render_template('form_contact.html', form = form)

if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5000, debug = True)
