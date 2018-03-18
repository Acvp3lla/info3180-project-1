from flask import Flask
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "+h1$1$@r@nd0ms3cr3tk3y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://luciano:password@localhost/thedatabase"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['postgresql://mbmqpbvauuqttt:4fcab97e61da14b4b2d52a64346bb3dfaaef1e063bf26fd5b9cfaeff81c4ce89@ec2-50-17-206-214.compute-1.amazonaws.com:5432/dfruam3ori6b22']

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         