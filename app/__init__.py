from flask import Flask
import os
import psycopg2
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "+h1$1$@r@nd0ms3cr3tk3y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://luciano:password@localhost/thedatabase"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

HEROKU_POSTGRESQL_RED_URL='postgresql://ikvjrhcxwgavte:81034d0ca3b4fdfa4ca15262835bfc4b7a1842ff4f0eaa00921319182255f758@ec2-54-163-246-193.compute-1.amazonaws.com:5432/daab9q8cgh9h2a'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_RED_URL']

db = SQLAlchemy(app)

conn = psycopg2.connect(HEROKU_POSTGRESQL_RED_URL, sslmode='require')

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         