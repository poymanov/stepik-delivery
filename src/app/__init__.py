from flask import Flask

from app.config import Config
from app.models import db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)
csrf.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)

from app.views import *
