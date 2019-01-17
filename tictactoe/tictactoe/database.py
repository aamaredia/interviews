from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    circle = db.Column(db.String(80), nullable=False)
    cross = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.JSON, primary_key=True)
