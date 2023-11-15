from flask import Flask, render_template
from sem3.task_1.models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill_db')
def fill_db():
    for i in range(3):
        faculty = Faculty(name=f'faculty_{i}')
        db.session.add(faculty)
        db.session.commit()
        for j in range(5):
            student = Student(name=f'name_{j}', surname=f'surname_{j}', faculty_id=faculty.id)
            db.session.add(student)
    db.session.commit()


@app.route('/students/')
def students():
    students = Student.query.all()
    return render_template('index.html', students=students)
