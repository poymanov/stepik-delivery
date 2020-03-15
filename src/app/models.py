from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

orders_meals_association = db.Table('orders_meals',
                                    db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                                    db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'))
                                    )


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    meals = db.relationship('Meal', back_populates='category')


class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    picture = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category')
    orders = db.relationship(
        "Order", secondary=orders_meals_association, back_populates='meals'
    )


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(32), nullable=False)
    orders = db.relationship('Order', back_populates='user')


class OrderStatus(enum.Enum):
    NEW = 'Новый'
    PROCESSED = 'Выполняется'
    COMPLETED = 'Готово'


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(OrderStatus), nullable=False)
    total = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')
    meals = db.relationship(
        "Meal", secondary=orders_meals_association, back_populates='orders'
    )
