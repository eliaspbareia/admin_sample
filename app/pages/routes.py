from flask import render_template

from app.pages import pages
from ..models import User, Categoria, Post, Foto

from app import admin, db
from flask_admin.contrib.sqla import ModelView

from .view import Usuarios

admin.add_view(Usuarios(User, db.session, category="Usuários"))
