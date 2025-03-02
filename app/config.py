import os
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename

# Configuration class
class Config:
    # General settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Default secret key, can be overridden via env variable
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')  # JWT secret key, can be overridden
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///mhondoro.db')  # Default SQLite URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable unnecessary modification tracking for SQLAlchemy
    
    # Upload settings
    UPLOADED_PHOTOS_DEST = os.getenv('UPLOADED_PHOTOS_DEST', 'app/static/uploads')  # Folder where photos are uploaded
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Alternative folder for uploads
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions for uploads

    # Mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')  # Email username from environment variable
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your-email-password')  # Email password from environment variable
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'your-email@gmail.com')  # Default sender email

    # Initialize the upload set for images
    photos = UploadSet('photos', IMAGES)

    def init_app(self, app):
        # Configure upload set
        configure_uploads(app, self.photos)
