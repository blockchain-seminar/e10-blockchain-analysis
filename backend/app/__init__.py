from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Include our Routes
        from . import views

        # Register Blueprints
        app.register_blueprint(views.bp)

        return app
