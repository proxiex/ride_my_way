from flask import Flask, jsonify
from config import config
from helpers.database import db_session
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    def intro():
        return jsonify('message', 'Welcome')

    app.add_url_rule(
        '/',
        'intro',
        view_func=intro
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
