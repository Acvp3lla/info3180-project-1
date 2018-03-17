from flask import Flask
import os
import psycopg2
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "+h1$1$@r@nd0ms3cr3tk3y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://luciano:password@localhost/thedatabase"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


DATABASE_URL = os.environ['postgresql://qderxnpbebfoos:76999dda31282cbd6572f2e23430fd52e446681a13e11500d34f6d0c0929e530@ec2-54-83-23-91.compute-1.amazonaws.com:5432/db4ocsifq4t575']

HEROKU_POSTGRESQL_MAUVE_URL='postgres://sinhdtleljegyk:62e462d49191214e3d52bee028628f41addde88045163ab246261490ea349459@ec2-54-83-23-91.compute-1.amazonaws.com:5432/d63q62hjlthpqg'
HEROKU_POSTGRESQL_PUCE_URL='postgres://kugbhwxkydhpxq:0c8118370526a9e617505f863aa669b5ab037f4102c8fb5470589ee4c5e61e06@ec2-54-83-23-91.compute-1.amazonaws.com:5432/d55991384ia8ih'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         