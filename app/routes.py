from flask import Flask, request, jsonify, Blueprint
from app import db  # Assuming you have SQLAlchemy initialized in app.py
from app.models import User, Equipment
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from app import photos
from app.models import Equipment

app = Flask(__name__)

# Secret key for JWT encoding and decoding
app.config['SECRET_KEY'] = 'your_secret_key'

# Utility functions for JWT
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

# Admin: List all users
@admin_api.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users])

# Admin: List all equipment
@admin_api.route('/equipment', methods=['GET'])
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

# Add image upload functionality for the equipment model.
@equipment_api.route('/equipment/<int:id>/upload_image', methods=['POST'])
def upload_image(id):
    equipment = Equipment.query.get(id)
    if not equipment:
        return jsonify({"message": "Equipment not found"}), 404

    if 'image' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400

    image = request.files['image']
    filename = photos.save(image)
    equipment.image_filename = filename
    db.session.commit()

    return jsonify({"message": "Image uploaded successfully", "filename": filename}), 200

# Equipment API (example route)
@app.route('/equipments', methods=['GET'])
def get_equipments():
    equipments = Equipment.query.all()
    return jsonify([{
        'id': eq.id, 'name': eq.name, 'category': eq.category, 
        'description': eq.description, 'price': eq.price, 'available': eq.available
    } for eq in equipments])

if __name__ == '__main__':
    app.run(debug=True)
