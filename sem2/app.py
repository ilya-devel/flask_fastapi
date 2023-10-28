from pathlib import PurePath, Path
import secrets

from flask import Flask, render_template, request, redirect, url_for, abort, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hello/")
def hello():
    return "HELLO FRIEND"


@app.route("/upload_img/", methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


@app.route("/log-in/", methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == "login" and password == "password":
            return f"Welcome {login}"
        return "Authorisation error"
    return render_template('log-in.html')


@app.route("/check-text/", methods=['GET', 'POST'])
def check_text():
    if request.method == 'POST':
        txt = request.form.get('text')
        return f"Length: {len(txt)}"
    return render_template('check-txt.html')


@app.route("/calc/", methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('a'))
        num2 = int(request.form.get('b'))
        oper = request.form.get('operation')
        if oper == 'add':
            return f"{num1 + num2}"
        elif oper == 'subtract':
            return f"{num1 - num2}"
        elif oper == 'multiply':
            return f"{num1 * num2}"
        elif oper == 'divide':
            return f"{num1 / num2}"
    return render_template('calc.html')


@app.route("/check-age/", methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= 18:
            return f"Welcome to the club, {name}"
        else:
            abort(403)
    return render_template('chk-age.html')


@app.errorhandler(403)
def forbidden_err(e):
    print(e)
    return "Вы слишком юны"


@app.route("/get-square/", methods=['POST', 'GET'])
def get_square():
    if request.method == 'POST':
        num = int(request.form.get('a'))
        return redirect(url_for('result', num=num))
    return render_template('square.html')


@app.route("/result/<int:num>")
def result(num):
    return f"Result: {num ** 2}"


@app.route("/greetings/", methods=['GET', 'POST'])
def greetings():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f"Welcome, {name}", "success")
        return redirect(url_for('greetings'))
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
