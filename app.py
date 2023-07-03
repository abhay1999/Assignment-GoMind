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
        
        with app.app_context():
            student = Student(name=name, college=college)
            db.session.add(student)
            db.session.commit()
        
    with app.app_context():
        students = Student.query.all()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
