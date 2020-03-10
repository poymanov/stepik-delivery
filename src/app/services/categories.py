from app.models import db, Category


def get_categories():
    return db.session.query(Category).all()
