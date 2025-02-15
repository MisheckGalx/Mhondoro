from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()  # Initialize Migrate

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Load configuration from the Config class
    app.config.from_object(Config)
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Initialize Flask-Migrate with app and db
    migrate.init_app(app, db)
    
    # Import and register blueprints or routes after app is created
    # from app import routes  # Uncomment if you have routes defined
    
    return app
