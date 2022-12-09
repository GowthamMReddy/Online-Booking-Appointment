from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

sqldb = SQLAlchemy()
DB_NAM = "database.sqldb"


def create_app():
    app = Flask(__name__)
    # Ideally for production secret key is not added
    app.config['SECRET_KEY'] = 'abcd abcdefg'
    
    return app
    
   # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAM}'
    sqldb.init_app(app)

    