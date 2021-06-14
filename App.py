from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootpasswordgiven@localhost/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    emailID = db.Column(db.String(100))
    department = db.Column(db.String(100))

    def __init__(self, name, age, emailID, department):
        self.name = name
        self.age = age
        self.emailID = emailID
        self.department = department

@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template('index.html', people = all_data)

@app.route('/insert', methods=['POST'])
def Insert():
    if request.method == 'POST':
       name = request.form['name']
       age = request.form['age']
       email = request.form['emailID']
       department = request.form['department']
    
    actualData = Data(name, age, email, department)
    db.session.add(actualData)
    db.session.commit()

    flash('Data Entered Successfully')
    return redirect(url_for('Index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.age = request.form['age']
        my_data.emailID = request.form['emailID']
        my_data.department = request.form['department']
        
        db.session.commit()
        
    flash('Data Updated Successfully!!!')
    return(redirect(url_for('Index')))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

