from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_admin import Admin
from app.admin import Usuarios
from app.models import User

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        # db.create_all()

        admin = Admin(app, name='microblog', template_mode='bootstrap3')
        admin.add_view(Usuarios(User, db.session))  
        
    return app