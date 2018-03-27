# -*- coding: utf-8 -*-
from flask import Flask

from api import commands
from api.settings import ProdConfig
from api.extensions import db, migrate
from api.exceptions import BaseException


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """

    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)

    register_extensions(app)
    register_errorhandlers(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    migrate.init_app(app, db)


def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(BaseException)(errorhandler)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
