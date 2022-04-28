from os import getenv

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow

from app import routes
from app.configs import database, jwt, migrations


def create_app():
    app = Flask(__name__)
    CORS(app)
    Marshmallow(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False

    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    routes.init_app(app)

    return app