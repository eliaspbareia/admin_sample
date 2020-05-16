from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate
import pymysql
from flask_admin import Admin

csrf_protect = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
admin = Admin( name='microblog', template_mode='bootstrap3')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    csrf_protect.init_app(app)

    admin.init_app(app)


        # admin.add_view(Usuarios(User, db.session))
        # admin.add_view(Fotos(Foto, db.session))
        #
        # path = join(basedir, 'uploads')
        # admin.add_view(FileAdmin(path, '/uploads/', name='Uploads'))

        # https://stackoverflow.com/questions/22064871/how-do-i-add-flask-admin-to-a-blueprint

    from .pages import pages as pages_blueprint
    app.register_blueprint(pages_blueprint, url_prefix='/pages')

    
    return app
