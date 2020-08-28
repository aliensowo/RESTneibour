import os
from flask import Flask

from .database import db, ma
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)
    with app.test_request_context():
        db.create_all()

    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    import app.neibour.controllers as neibour

    app.register_blueprint(neibour.module)

    return app




