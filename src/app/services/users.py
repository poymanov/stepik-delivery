from app.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session


def register(form):
    user = User()
    user.name = form.name.data
    user.email = form.email.data
    user.password = generate_password_hash(form.password.data)
    user.address = form.address.data
    user.role = 'user'
    db.session.add(user)
    db.session.commit()


def login(form):
    user = db.session.query(User).filter(User.email == form.email.data).first()
    if user and check_password_hash(user.password, form.password.data):
        session['user'] = {'id': user.id, 'role': user.role}
        return True
    else:
        return False


def logout():
    session.pop('user')
