from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    group = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'User({self.name}, {self.surname}, {Faculty.query.filter_by(id=self.faculty_id).first()})'

    def __str__(self):
        return f'{self.name} {self.surname} посещает факультет {Faculty.query.filter_by(id=self.faculty_id).first()}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    student_id = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty({self.name})'

    def __str__(self):
        return f'{self.name}'
