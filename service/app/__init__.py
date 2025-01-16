from flask import Flask
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register blueprints
    from .routes.blueprints import webpage_bps

    for bp in webpage_bps:
        app.register_blueprint(bp, url_prefix="/")

    return app
