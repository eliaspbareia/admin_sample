from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config():

    FLASK_ADMIN_SWATCH = 'cerulean'

    SECRET_KEY = environ.get('SECRET_KEY') or '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

    FLASKY_MAIL_SUBJECT_PREFIX = '[Gomes]'
    FLASKY_MAIL_SENDER = 'GOMES ADMIN <eliaspbareia@gmail.com>'
    FLASKY_ADMIN = environ.get('ADMIN')
    CSRF_ENABLED = True

    # https://www.freemysqlhosting.net/account/
    # http://www.phpmyadmin.co/
    # account number 416135
    # database host: sql10.freemysqlhosting.net
    # database name: sql10341015
    # Database Username: sql10341015
    # Password: 4nP1v5d8Dw
    # Port number: 3306
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bot901@localhost:3306/botanico'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql10341015:4nP1v5d8Dw@sql10.freemysqlhosting.net:3306/sql10341015'
    SQLALCHEMY_ECHO = True

    POSTS_PER_PAGE = 3
