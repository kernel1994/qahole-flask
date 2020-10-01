import os

from flask import Flask
import flask_restful as restful

from api.common import db
from api.resources.qahole import QaHole
from api.resources.qahole_solo import QaHoleSolo
from api.resources.qa import Qa
from api.resources.treehole import Treehole
from api.resources.tucao import Tucao
from api.resources.random import Random


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'data-sqlite3.db'),
    )

    api = restful.Api(app, prefix='/api')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init(app)

    # Resourceful Routing
    api.add_resource(QaHole, '/qahole')
    api.add_resource(QaHoleSolo, '/qahole/<int:comment_id>')
    api.add_resource(Qa, '/qa', '/qa/<int:comment_id>')
    api.add_resource(Treehole, '/treehole', '/treehole/<int:comment_id>')
    api.add_resource(Tucao, '/tucao/<int:comment_parent>')
    api.add_resource(Random, '/random', '/random/<int:number>')

    return app
