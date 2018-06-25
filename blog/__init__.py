from flask import Flask
from flask_pymongo import PyMongo, pymongo
from pymongo import MongoClient
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

#MAIL_PWD and MAIL_USER are set using nano .bash_profile in the home dir

app = Flask(__name__)
app.config['SECRET_KEY']= os.environ.get('MAIL_PWD')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PWD')
mail = Mail(app)

from blog import routes
