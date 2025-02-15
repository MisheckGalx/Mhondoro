from flask import Blueprint, jsonify
from app.models import Equipment

main = Blueprint('main', __name__)

@main.route('/equipments', methods=['GET'])
def get_equipments():
    equipments = Equipment.query.all()
    return jsonify([{
        'id': eq.id, 'name': eq.name, 'category': eq.category, 
        'description': eq.description, 'price': eq.price, 'available': eq.available
    } for eq in equipments])
