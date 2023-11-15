from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    group = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    grades = db.relationship('Grade', backref='grades', lazy=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __str__(self):
        return f'{Student.query.get(self.student_id)} - {self.name}: {self.grade}'

