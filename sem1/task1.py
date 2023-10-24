from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "HELLO WORLD!"


@app.route("/about/")
def about():
    return "ABOUT"


@app.route("/contact/")
def contact():
    return "CONTACT"


@app.route("/<int:num1>/<int:num2>/")
def summarize(num1, num2):
    return str(num1 + num2)


@app.route("/get-length-row/<string:row>/")
def get_length_row(row):
    return str(len(row))


@app.route("/get-html/")
def get_html():
    return """
    <h1>HELLO!</h1>
    """


@app.route("/students/")
def get_info_about_students():
    students = [
        {"name": "alex", "surname": "black", "age": 17, "rating": 4.5},
        {"name": "alex", "surname": "black", "age": 17, "rating": 4.5},
        {"name": "alex", "surname": "black", "age": 17, "rating": 4.5},
        {"name": "alex", "surname": "black", "age": 17, "rating": 4.5},
        {"name": "alex", "surname": "black", "age": 17, "rating": 4.5}
    ]
    return render_template("students.html", students=students)


@app.route("/news/")
def news():
    news_ = [
        {"title": "TITLE", "date": "24.10.2023",
         "description": "some newssome newssome newssome newssome newssome newssome newssome newssome newssome \
         newssome newssome newssome newssome newssome newssome news"},
        {"title": "TITLE", "date": "24.10.2023",
         "description": "some newssome newssome newssome newssome newssome newssome newssome newssome newssome \
         newssome newssome newssome newssome newssome newssome news"},
        {"title": "TITLE", "date": "24.10.2023",
         "description": "some newssome newssome newssome newssome newssome newssome newssome newssome newssome \
         newssome newssome newssome newssome newssome newssome news"},
        {"title": "TITLE", "date": "24.10.2023",
         "description": "some newssome newssome newssome newssome newssome newssome newssome newssome newssome \
         newssome newssome newssome newssome newssome newssome news"},
        {"title": "TITLE", "date": "24.10.2023",
         "description": "some newssome newssome newssome newssome newssome newssome newssome newssome newssome \
         newssome newssome newssome newssome newssome newssome news"},
    ]
    return render_template("news2.html", news=news_)


if __name__ == '__main__':
    app.run(debug=True)
