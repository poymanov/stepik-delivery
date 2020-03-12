from app.models import db, Category
import random


def get_categories():
    return db.session.query(Category).all()


def get_categories_with_random_meals(count):
    categories_data = []

    categories = db.session.query(Category).all()

    for category in categories:
        categories_data.append({'category': category, 'meals': random.sample(category.meals, count)})

    return categories_data
