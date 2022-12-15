from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

sqldb = SQLAlchemy()
DB_NAM = "database.sqldb"


def create_app():
    app = Flask(__name__)
    # Ideally for production secret key is not added
<<<<<<< HEAD
   # webapp.config['SECRET_KEY'] = 'abcd abcdefg'
   # webapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAM}'
    #sqldb.init_app(webapp)
    return webapp
=======
    app.config['SECRET_KEY'] = 'abcd abcdefg'
    
    return app
    
   # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAM}'
    sqldb.init_app(app)

    
>>>>>>> 86851063a5579339d1ef2fbdfba77bec4f7270e5
