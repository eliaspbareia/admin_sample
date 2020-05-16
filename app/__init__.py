from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate
import pymysql
from flask_admin import Admin
from app.admin import Usuarios
from app.models import User

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    
    admin = Admin(app, name='microblog', template_mode='bootstrap3')

    with app.app_context():
        # db.create_all()
        admin.add_view(Usuarios(User, db.session))

    return app
