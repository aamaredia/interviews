import logging

from flask import Flask
from flask_restful import Api

from tictactoe import api

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
db.init_app(app)

rest_api = Api(app)

rest_api.add_resource(api.Games, '/api/games')
rest_api.add_resource(api.Game, '/api/games/<id>')


if __name__ = '__main__':
    app.run(port='5000')
