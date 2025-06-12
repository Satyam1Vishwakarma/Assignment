from flask import Flask
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from config import Config

mongo = PyMongo()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    ma.init_app(app)

    from app.routes.users import user_bp
    app.register_blueprint(user_bp, url_prefix="/api")

    from app.errors import register_error_handlers
    register_error_handlers(app)

    return app