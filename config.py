import os
from werkzeug.utils import secure_filename # Updated import
from flask_reuploaded import UploadSet, configure_uploads, IMAGES

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///mhondoro.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload settings
    UPLOADED_PHOTOS_DEST = os.getenv('UPLOADED_PHOTOS_DEST', 'app/static/uploads')

    # Mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your-email-password')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'your-email@gmail.com')

# Initialize UploadSet for image files
photos = UploadSet('photos', IMAGES)
