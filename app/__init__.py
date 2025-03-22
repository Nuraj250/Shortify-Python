from flask import Flask
from .routes import url_shortener_routes
from .config import Config
from pymongo import MongoClient

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Make db accessible globally
    app.db = db

    # Register routes
    app.register_blueprint(url_shortener_routes)

    return app

