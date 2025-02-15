from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Set the configuration values
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mhondoro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    return app
