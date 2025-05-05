from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mangaka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    anime = db.relationship('Anime', backref='creator', lazy=True)

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    episodes = db.Column(db.Integer)
    status = db.Column(db.String(20))
    mangaka_id = db.Column(db.Integer, db.ForeignKey('mangaka.id'), nullable=False)
