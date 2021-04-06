from app.models.tables import User
from app.controllers import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager

app = Flask(__name__, template_folder='templates')
# app.config.from_object('config')

db = SQLAlchemy(app)
# app.config("SQLALCHEMY_TRACK_MODIFICATIONS ")
