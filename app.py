from flask import Flask, jsonify
from config import config
from utils.database import db_session
from flask_cors import CORS
# from flask.ext.bcrypt import Bcrypt
from flask_bcrypt import Bcrypt

from api.user.views import user_view

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)


def index():
        return jsonify('message', 'Welcome')


def create_app(config_name):
    base_url = '/api/v1'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.add_url_rule(
        '/',
        'index',
        index
    )

    app.add_url_rule(
        base_url+'/users/signup',
        'create',
        view_func=user_view.create,
        methods=['POST']
    )

    app.add_url_rule(
        base_url+'/user/login',
        'login',
        view_func=user_view.login,
        methods=['POST']
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
