from app.models import Category, Meal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import csv

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
session = Session()

categories_data = csv.DictReader(open('import_data/categories.csv'))
meals_data = csv.DictReader(open('import_data/items.csv'))

for category_item in categories_data:
    session.add(Category(id=category_item.get('id'), title=category_item.get('title')))

session.commit()

for meals_item in meals_data:
    session.add(Meal(id=meals_item.get('id'), title=meals_item.get('title'), price=meals_item.get('price'),
                     description=meals_item.get('description'), picture=meals_item.get('picture'),
                     category_id=meals_item.get('category_id')))

session.commit()
