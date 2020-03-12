from flask import Flask

from app.config import Config
from app.models import db, User, Meal, Category, Order
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Meal, db.session))
admin.add_view(ModelView(Order, db.session))

from app.views import *


