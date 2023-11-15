from flask import Flask, render_template
from sem3.task_2.models import db, Book, Author
from random import choices, randint, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3_task2.sqlite'
db.init_app(app)


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill_db')
def fill_db():
    names = ['Jack', 'Mary', 'Barbara', 'Liza']
    surnames = ['Black', 'Smith', 'Brown']
    verbs = ['write', 'fix', 'make']
    nouns = ['book', 'car', 'knife', 'house']
    for _ in range(3):
        author = Author(name=choice(names), surname=choice(surnames))
        db.session.add(author)
    db.session.commit()
    for _ in range(10):
        authors = Author.query.all()
        book = Book(
            title=f'How to {choice(verbs)} the {choice(nouns)}',
            year_published=randint(1992, 2024),
            number_copies=randint(50, 200) * 1000,
            author_id=choice(authors).id
        )
        db.session.add(book)
    db.session.commit()
