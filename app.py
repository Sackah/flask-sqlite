from flask import Flask, request, render_template
import sqlite3
from helpers import validate_required

app = Flask(__name__)

# home page
@app.route('/')
def home():
    return render_template('home.html')

# form for adding a new student to the db
@app.route('/enternew')
def enternew():
    return render_template('student.html')

# add a student to the db
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        required_fields = [
            'nm', 'city', 'add', 'zip'
        ]
        # validation
        if not validate_required(required_fields):
            try:
                with sqlite3.connect("students.sqlite") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO students (name, addr, city, zip) VALUES (?, ?, ?, ?)", 
                                (request.form.get('nm'), request.form.get('add'),
                                request.form.get('city'), request.form.get('zip'))
                               )
                    con.commit()
                    msg = "Record successfully added to the db"
            except Exception as e:
                con.rollback()
                msg = "An error occured in the insertion: " + str(e)
            finally:
                con.close()
                return render_template('result.html', msg=msg)
        else:
            return validate_required(required_fields)
    else:
        return render_template('home.html')

@app.route('/list')
def list():
    try:
        conn = sqlite3.connect("students.sqlite")
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute("SELECT * FROM students") 

        rows = cur.fetchall()
        return render_template('list.html', rows=rows)
    except Exception as e:
        msg = "An error occured while trying to retrieve data: " + str(e)
        return render_template("result.html", msg=msg)
    finally:
        conn.close()

# select a specific row in the database then load an edit form 
@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        try:
            id = request.form["id"]

            conn = sqlite3.connect("students.sqlite")
            conn.row_factory = sqlite3.Row

            cur = conn.cursor()
            cur.execute("SELECT * FROM students where id = ? ", id)

            rows = cur.fetchall()
            return render_template("edit.html", rows=rows)
        except Exception as e:
            id=None
            msg = "An error occured while trying to retrieve data: " + str(e)
            return render_template("result.html", msg=msg)
        finally:
            conn.close()

@app.route('/editrec')
def editrec():
    return

@app.route("/delete")
def delete():
    return
