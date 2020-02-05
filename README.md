


cd /mnt/g/2020_working/coding/flask_forms_SQLITE_demo

conda deactivate
which python3
python3 --version
python3 -m venv env
source env/bin/activate
(env)$ which python3
(env)$ python3 --version
(env)$ pip install flask
(env)$ pip freeze

pip install flask-wtf


--------------------------notes ------------------------------------------------
If you want to retrieve POST data,

first_name = request.form.get("firstname")
- If you want to retrieve GET (query string) data,

first_name = request.args.get("firstname")
- Or if you don't care/know whether the value is in the query string or in the post data,

first_name = request.values.get("firstname").
- request.values is a CombinedMultiDict that combines Dicts from request.form and request.args.
--------------------------notes ------------------------------------------------



https://www.tutorialspoint.com/flask/flask_sqlite.htm



sudo apt install sqlite3
sqlite3 database.db
.tables
.schema students

sqlite3 students.db
.tables
.schema students
SELECT * FROM students;



pip install flask-sqlalchemy

student = students('fred', 'fred city', 'fred address', 'fred pin')
db.session.add(student)
db.session.commit()
