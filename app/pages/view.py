from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField
from flask import request, Response, url_for
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash



class Usuarios(ModelView):
    column_list = ('nome', 'username', 'email')
    column_searchable_list = ('nome','username', 'email')
    can_create = True
    form_extra_fields = {
        'password': PasswordField('Password')
    }

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method='sha256')
