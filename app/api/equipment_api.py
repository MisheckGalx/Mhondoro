from flask import Blueprint, request, jsonify
from app import db
from app.models import Equipment, Category
from app.services.equipment_service import EquipmentService

equipment_api = Blueprint('equipment_api', __name__)

# Create Category
@equipment_api.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    name = data.get('name')

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()

    return jsonify({"message": "Category created", "category": category.name}), 201

# Get all Categories
@equipment_api.route('/category', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories])

# Add pagination functionality to get equipment and reviews
@equipment_api.route('/equipment', methods=['GET'])
def get_all_equipment():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    equipment_list = Equipment.query.paginate(page, per_page, False)
    return jsonify({
        'equipments': [{
            'id': equip.id,
            'name': equip.name,
            'description': equip.description
        } for equip in equipment_list.items],
        'total': equipment_list.total,
        'pages': equipment_list.pages
    })

# Create Equipment with Category
@equipment_api.route('/equipment', methods=['POST'])
def create_equipment():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    user_id = data.get('user_id')
    category_id = data.get('category_id')

    new_equipment = Equipment(name=name, description=description, user_id=user_id, category_id=category_id)
    db.session.add(new_equipment)
    db.session.commit()

    return jsonify({"message": "Equipment created", "equipment": new_equipment.name}), 201

# Get Equipment by Category
@equipment_api.route('/equipment/category/<int:category_id>', methods=['GET'])
def get_equipment_by_category(category_id):
    equipment_list = Equipment.query.filter_by(category_id=category_id).all()
    return jsonify([{
        'id': equip.id,
        'name': equip.name,
        'description': equip.description,
        'category': equip.category.name
    } for equip in equipment_list])

@equipment_api.route('/equipment/search', methods=['GET'])
def search_equipment():
    query = request.args.get('query', '')
    category_id = request.args.get('category_id', None)

    query_filter = Equipment.query.filter(Equipment.name.ilike(f'%{query}%'))
    if category_id:
        query_filter = query_filter.filter_by(category_id=category_id)

    results = query_filter.all()
    return jsonify([{
        'id': equip.id,
        'name': equip.name,
        'description': equip.description,
        'category': equip.category.name
    } for equip in results])

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Review {self.rating}>"

# Add a review
@equipment_api.route('/equipment/<int:equipment_id>/review', methods=['POST'])
def add_review(equipment_id):
    data = request.get_json()
    rating = data.get('rating')
    comment = data.get('comment')
    user_id = data.get('user_id')

    review = Review(rating=rating, comment=comment, equipment_id=equipment_id, user_id=user_id)
    db.session.add(review)
    db.session.commit()

    return jsonify({"message": "Review added", "rating": review.rating}), 201

# Get all reviews for an equipment
@equipment_api.route('/equipment/<int:equipment_id>/reviews', methods=['GET'])
def get_reviews(equipment_id):
    reviews = Review.query.filter_by(equipment_id=equipment_id).all()
    return jsonify([{
        'id': review.id,
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at
    } for review in reviews])
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # New fields for profile
    location = db.Column(db.String(100), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    bio = db.Column(db.String(500), nullable=True)

    # Relationship with equipment
    equipments = db.relationship('Equipment', backref='owner', lazy=True)
