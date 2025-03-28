from flask import Flask, render_template
from .routes import url_shortener_routes
from .config import Config
from pymongo import MongoClient

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )
    app.config.from_object(Config)
    app.db = db

    # Register Blueprint
    app.register_blueprint(url_shortener_routes)

    # Custom 404 Page
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
