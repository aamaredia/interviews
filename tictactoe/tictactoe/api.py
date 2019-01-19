import random
import json

from flask_restful import Resource, reqparse

from tictactoe import models
from tictactoe.database import db


EMPTY_BOARD = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

EMPTY = -1
CIRCLE = 0
CROSS = 1

BOARD_LOOKUP = {
    CIRCLE: 'O',
    CROSS: 'X',
    EMPTY: None,
}

def pretty_board(board):
    pretty_board = []
    for row in board:
        pretty_board.append([BOARD_LOOKUP[space] for space in row])
    return pretty_board


class Games(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('player1', type=str, help='Player one')
    parser.add_argument('player2', type=str, help='Player two')

    def get(self):
        return models.Games.query.all()

    def post(self):
        args = self.parser.parse_args()
        circle, cross = random.sample([args['player1'], args['player2']], 2)
        new_game = models.Games(
            circle=circle,
            cross=cross,
            board=EMPTY_BOARD,
            next_turn=random.choice([circle, cross]),
        )
        db.session.add(new_game)
        db.session.commit()
        return {
                'id': new_game.id,
                'circle': new_game.circle,
                'cross': new_game.cross,
                'board': pretty_board(new_game.board),
                'next_turn': new_game.next_turn,
                'status': new_game.status,
        }

class Game(Resource):
    def get(self, id):
        return None

    def post(self):
        return None
