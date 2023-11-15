from flask import Flask, render_template, request, redirect, url_for, session
from sem3.task_5.models import db, User
from flask_wtf.csrf import CSRFProtect
from secrets import token_hex
from sem3.task_5.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3_task5.sqlite'
app.config['SECRET_KEY'] = token_hex()
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        login = form.login.data
        email = form.email.data
        birthday = form.birthday.data
        agree = form.agree.data
        password = form.password.data
        if not User.query.filter_by(login=login).first() and not User.query.filter_by(email=email).first():
            user = User(login=login, email=email, birthday=birthday, personal_agree=agree)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            session['user'] = login
            return redirect(url_for('index'))
        else:
            msg = ''
            if User.query.filter_by(login=login).first():
                msg = 'Данный логин уже используется'
            if User.query.filter_by(email=email).first():
                msg = 'Данная почта уже используется'
            return render_template('registration.html', form=form, msg=msg)
    return render_template('registration.html', form=form)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    msg = ''
    if request.method == 'POST' and form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        if User.query.filter_by(login=login).first():
            if User.query.filter_by(login=login).first().check_password(password):
                session['user'] = User.query.filter_by(login=login).first().login
                return redirect(url_for('index'))
            else:
                msg = 'Invalid password'
                return render_template('registration.html', form=form, msg=msg)
        else:
            msg = 'Unknown login'
            return render_template('registration.html', form=form, msg=msg)
    return render_template('registration.html', form=form)


@app.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')
