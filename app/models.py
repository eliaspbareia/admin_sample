from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(80))
    password = db.Column(db.String(255))    
    update = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}'.format(self.username)

class Post(db.Model):
    # id author title body content thumb post_date
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(80), index=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text,  nullable=False)
    pub_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    thumb = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    category = db.relationship('Categoria', backref=db.backref('posts', lazy=True))
    fotos = db.relationship('Foto', backref='post', lazy='dynamic')

    def __repr__(self):
        return 'Post {}'.format(self.title)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Foto (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo = db.Column(db.String(30))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
