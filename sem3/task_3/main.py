from flask import Flask, render_template
from sem3.task_3.models import db, Student, Grade
from random import randint, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3_task3.sqlite'
db.init_app(app)


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill_db')
def fill_db():
    names = ['Jack', 'Mary', 'Barbara', 'Liza']
    surnames = ['Black', 'Smith', 'Brown']
    subjects = ['Chemistry', 'Math', 'History']
    for _ in range(5):
        name = choice(names)
        surname = choice(surnames)
        db.session.add(Student(
            name=name,
            surname=surname,
            group=f'{randint(1, 4)}{choice(["A", "B", "C"])}',
            email=f'{name}_{surname}@myschool.site'
        ))
    db.session.commit()
    students = Student.query.all()
    for _ in range(20):
        db.session.add(Grade(
            name=choice(subjects),
            grade=randint(1, 100 + 1),
            student_id=choice(students).id
        ))
    db.session.commit()
