from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Имя', [InputRequired(), Length(min=3, message='Не менее 3 символов')])
    email = StringField('Электропочта', [InputRequired(), Length(min=5, message='Не менее 5 символов'),
                                         Email('Неверный формат электронного адреса')])
    password = PasswordField('Пароль',
                             [InputRequired(), Length(min=8, message='Пароль должен быть не менее 8 символов')])
    password_confirm = PasswordField("Повторение пароля",
                                     [InputRequired(), EqualTo('password', message='Пароли не совпадают')])
    address = TextAreaField('Адрес', [InputRequired(), Length(min=5, message='Не менее 5 символов')])


class LoginForm(FlaskForm):
    email = StringField('Электропочта', [InputRequired(), Length(min=5, message='Не менее 5 символов'),
                                         Email('Неверный формат электронного адреса')])
    password = PasswordField('Пароль',
                             [InputRequired(), Length(min=8, message='Пароль должен быть не менее 8 символов')])


class OrderForm(FlaskForm):
    name = StringField('Ваше имя', [InputRequired(), Length(min=3, message='Не менее 3 символов')])
    email = StringField('Электропочта', [InputRequired(), Length(min=5, message='Не менее 5 символов'),
                                         Email('Неверный формат электронного адреса')])
    phone = StringField('Телефон', [InputRequired(), Length(min=3, message='Не менее 3 символов')])
    address = TextAreaField('Адрес', [InputRequired(), Length(min=5, message='Не менее 5 символов')])
