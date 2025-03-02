import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

# Initialize the Flask app and extensions
app = Flask(__name__)

# Secret key for JWT encoding and decoding
app.config['SECRET_KEY'] = 'your_secret_key'

# Database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mhondoro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Upload settings
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize the extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, default=True)
    image_filename = db.Column(db.String(120), nullable=True)

# JWT Utility Functions
def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    except Exception as e:
        return str(e)

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token.'

# Routes

# Admin: List all users
@app.route('/admin/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users])

# Admin: List all equipment
@app.route('/admin/equipment', methods=['GET'])
def list_equipment():
    equipment_list = Equipment.query.all()
    return jsonify([{
        'id': equip.id,
        'name': equip.name,
        'description': equip.description
    } for equip in equipment_list])

# User Registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    hashed_password = generate_password_hash(password, method='sha256')  # Hash password before storing
    new_user = User(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "username": new_user.username}), 201

# User Login (JWT Token Generation)
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):  # Check hashed password
        token = encode_auth_token(user.id)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Equipment API (example route)
@app.route('/equipments', methods=['GET'])
def get_equipments():
    equipments = Equipment.query.all()
    return jsonify([{
        'id': eq.id, 'name': eq.name, 'category': eq.category, 
        'description': eq.description, 'price': eq.price, 'available': eq.available
    } for eq in equipments])

# Image Upload for Equipment
@app.route('/equipment/<int:id>/upload_image', methods=['POST'])
def upload_image(id):
    equipment = Equipment.query.get(id)
    if not equipment:
        return jsonify({"message": "Equipment not found"}), 404

    if 'image' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
    equipment.image_filename = filename
    db.session.commit()

    return jsonify({"message": "Image uploaded successfully", "filename": filename}), 200

# File upload route (for general use)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 201
    return jsonify({"message": "Invalid file type"}), 400

# Allowed file type checker
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

if __name__ == '__main__':
    app.run(debug=True)
