from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

# GET: страница входа
@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# POST: обработка входа
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Пожалуйста, проверьте данные и повторите попытку')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

# GET: страница регистрации
@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

# POST: обработка регистрации
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Такой адрес уже существует')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, login=login, password=generate_password_hash(password, method='pbkdf2:sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

# Выход
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
