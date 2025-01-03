from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/baby_feeding_tracker.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

from app import routes,models
from app.routes import app as routes_blueprint

app.register_blueprint(routes_blueprint)

with app.app_context():
    inspector = inspect(db.engine)
    if 'feeding_record' not in inspector.get_table_names():
      db.create_all()