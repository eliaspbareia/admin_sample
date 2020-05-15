from os import environ, path


class Config():

    FLASK_ADMIN_SWATCH = 'cerulean'

    SECRET_KEY = environ.get('SECRET_KEY') or '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

    FLASKY_MAIL_SUBJECT_PREFIX = '[Gomes]'
    FLASKY_MAIL_SENDER = 'GOMES ADMIN <eliaspbareia@gmail.com>'
    FLASKY_ADMIN = environ.get('ADMIN')
    CSRF_ENABLED = True

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senha@localhost:3306/dababasename'
    SQLALCHEMY_ECHO = True
    
    POSTS_PER_PAGE = 3

