from flask import render_template
from app import app
import app.services.categories as categories_service


@app.route('/')
def index():
    return render_template('index.html', categories=categories_service.get_categories())
