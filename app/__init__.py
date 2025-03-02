import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
from app.config import Config

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()
photos = UploadSet('photos', IMAGES)

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Load the configuration from the Config class
    app.config.from_object(Config)

    # Ensure migration directory exists
    if not os.path.exists(os.path.join(app.instance_path, 'migrations')):
        os.makedirs(os.path.join(app.instance_path, 'migrations'))

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize the upload set for images
    configure_uploads(app, photos)

    # You can add routes or blueprints here if needed later
    # Example: from app import views

    return app

# Make sure the app is running correctly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
