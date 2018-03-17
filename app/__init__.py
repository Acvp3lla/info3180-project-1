from flask import Flask
import os
import psycopg2
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "+h1$1$@r@nd0ms3cr3tk3y"
#postgresql://luciano:password@localhost/thedatabase
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qderxnpbebfoos:76999dda31282cbd6572f2e23430fd52e446681a13e11500d34f6d0c0929e530@ec2-54-83-23-91.compute-1.amazonaws.com:5432/db4ocsifq4t575"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


DATABASE_URL = os.environ['']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         