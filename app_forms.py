from flask import Flask, render_template, request, flash
from forms import ContactForm


app = Flask(__name__)
app.secret_key = 'development key'


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
