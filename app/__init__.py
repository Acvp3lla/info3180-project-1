from flask import Flask
import os
import psycopg2
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "+h1$1$@r@nd0ms3cr3tk3y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://luciano:password@localhost/thedatabase"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning




db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         