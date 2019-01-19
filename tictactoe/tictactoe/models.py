from tictactoe.database import db


class Games(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    circle = db.Column(db.String(80), nullable=False)
    cross = db.Column(db.String(80), nullable=False)
    board = db.Column(db.ARRAY(db.Integer, dimensions=2, zero_indexes=True), nullable=False)
    next_turn = db.Column(db.String(5), nullable=False)
    status = db.Column(db.Boolean, nullable=False, server_default='f')
