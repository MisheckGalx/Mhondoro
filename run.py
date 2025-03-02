from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from app.api.inquiries_api import inquiries_bp
from app.api.reviews_api import reviews_bp

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Load the configuration from the Config class
    app.config.from_object(Config)

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(inquiries_bp, url_prefix="/api/inquiries")
    app.register_blueprint(reviews_bp, url_prefix="/api/reviews")

    return app

# Create the Flask app using the factory function
app = create_app()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
