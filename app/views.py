from flask import redirect, url_for, request
from wtforms import fields, validators, PasswordField
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash

from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers, expose
import flask_login as login

from flask_sqlalchemy import SQLAlchemy
from app.models import User, db


class myAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(myAdminIndexView, self).index()

    @expose('/login/', methods=('GET','POST'))
    def login_view(self):
        form = LoginForm()

        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Caso não tenha um login e senha, contate o administrador.'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(myAdminIndexView, self).index()

    @expose('/logout')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

class LoginForm(FlaskForm):
    username = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Usuário inválido')

        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Senha inválida')

    def get_user(self):

        return db.session.query(User).filter_by(username=self.username.data).first()


class UserView(ModelView):
    column_list = ('nome', 'username', 'email')
    column_searchable_list = ('nome','username', 'email')
    can_create = True
    form_extra_fields = {
        'password': PasswordField('Password')
    }

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method='sha256')


    def is_accessible(self):
        return login.current_user.is_authenticated


    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))
