import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Ensure the correct import path

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints if any
    from app.routes import main
    app.register_blueprint(main)

    return app
