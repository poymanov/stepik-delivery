from app.models import db, Meal


def get_by_id(id):
    return db.session.query(Meal).get(id)
