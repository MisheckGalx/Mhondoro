from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Initialize the app, db, and migrate
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Initialize migration
migrate = Migrate(app, db)

# Initialize your routes
from app import views

# Initialize other extensions like login manager, etc.
