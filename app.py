from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    college = db.Column(db.String(100))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        
        student = Student(name=name, college=college)
        db.session.add(student)
        db.session.commit()
        
    students = Student.query.all()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    db.create_all()
    app.run()
