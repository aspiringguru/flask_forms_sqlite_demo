from flask import Flask, render_template, request, flash
from forms import ContactForm
import sqlite3 as sql



app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')


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
