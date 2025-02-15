from app import db
from app.models import User, Equipment
from app import create_app

app = create_app()

with app.app_context():
    db.create_all()
