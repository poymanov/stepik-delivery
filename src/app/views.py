from flask import render_template, redirect, session, request, flash
from app import app
import app.services.categories as categories_service
import app.services.users as users_service
import app.services.cart as cart_service
from app.forms import RegisterForm, LoginForm
from functools import wraps


def user_guest(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user'):
            return redirect('/')
        return f(*args, **kwargs)

    return decorated_function


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user'):
            return redirect('/login')
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def index():
    return render_template('index.html', categories=categories_service.get_categories())


@app.route('/register', methods=['GET', 'POST'])
@user_guest
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        users_service.register(form)
        return redirect('/')
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@user_guest
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if users_service.login(form):
            return redirect('/')
        else:
            form.email.errors.append('Неверный email или пароль')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
def logout():
    users_service.logout()
    return redirect('/')


@app.route('/account', methods=['GET'])
@login_required
def account():
    return render_template('account.html')


@app.route('/cart', methods=['GET'])
def cart():
    return render_template('cart.html', cart=cart_service.get_cart())


@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    cart_service.add_to_cart(request.form.get('id'))
    return redirect('/cart')


@app.route('/delete-from-cart', methods=['POST'])
def delete_from_cart():
    cart_service.delete_from_cart(request.form.get('id'))
    flash('Блюдо удалено из корзины')
    return redirect('/cart')
