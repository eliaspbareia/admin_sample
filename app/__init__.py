from flask import Flask,current_app, redirect, url_for, request
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate
import pymysql
from flask_admin import Admin

import flask_login as login
from .views import myAdminIndexView, UserView

from .models import User

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


admin = Admin(name='microblog', index_view=myAdminIndexView(), base_template='master.html')

def init_login(app):

    login_manager = login.LoginManager()
    login_manager.init_app(app)

    from .models import  User
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    migrate.init_app(app, db)

    csrf.init_app(app)

    admin.init_app(app)

    init_login(app)

    admin.add_view(UserView(User, db.session))

    return app
