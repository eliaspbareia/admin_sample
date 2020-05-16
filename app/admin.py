from flask_admin.contrib.sqla import ModelView
from flask import request, Response, url_for
from werkzeug.exceptions import HTTPException


class Usuarios(ModelView):
    column_list = ('id', 'username', 'email')
    can_create = True
