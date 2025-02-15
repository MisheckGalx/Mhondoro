from flask import Blueprint, request, jsonify
from .models import db, Equipment

equipment_bp = Blueprint('equipment', __name__)

# Add new equipment
@equipment_bp.route('/', methods=['POST'])
def add_equipment():
    data = request.get_json()
    name = data['name']
    description = data['description']
    category = data['category']
    price = data['price']

    new_equipment = Equipment(name=name, description=description, category=category, price=price)
    db.session.add(new_equipment)
    db.session.commit()

    return jsonify({"message": "Equipment added successfully!"}), 201

# Get all equipment
@equipment_bp.route('/', methods=['GET'])
def get_all_equipment():
    equipment_list = Equipment.query.all()
    return jsonify([e.as_dict() for e in equipment_list]), 200

# Update equipment
@equipment_bp.route('/<int:id>', methods=['PUT'])
def update_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    data = request.get_json()

    equipment.name = data['name']
    equipment.description = data['description']
    equipment.category = data['category']
    equipment.price = data['price']

    db.session.commit()

    return jsonify({"message": "Equipment updated successfully!"}), 200

# Delete equipment
@equipment_bp.route('/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = Equipment.query.get_or_404(id)
    db.session.delete(equipment)
    db.session.commit()

    return jsonify({"message": "Equipment deleted successfully!"}), 200

from geopy.geocoders import Nominatim

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    # Optional: Automatically geocode location on creation
    def set_location(self, location_name):
        geolocator = Nominatim(user_agent="mhondoro_app")
        location = geolocator.geocode(location_name)
        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude
