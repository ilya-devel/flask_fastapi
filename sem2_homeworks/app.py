import secrets

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route("/")
def index():
    if request.cookies.get('name'):
        name = request.cookies.get('name')
        return render_template('index.html', name=name)
    return render_template('index.html')


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        resp = redirect(url_for('index'))
        resp.set_cookie('name', name, max_age=60 * 60)
        return resp
    return render_template('login.html')


@app.route("/logout/")
def logout():
    resp = redirect(url_for('login'))
    resp.set_cookie('name', '', max_age=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
