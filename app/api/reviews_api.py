from flask import Blueprint, request, jsonify
from app.services.review_service import create_review, get_reviews
from flask_jwt_extended import jwt_required, get_jwt_identity

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/", methods=["POST"])
@jwt_required()
def add_review():
    data = request.get_json()
    user_id = get_jwt_identity()
    response = create_review(user_id, data)
    return jsonify(response), response.get("status", 400)

@reviews_bp.route("/<int:supplier_id>", methods=["GET"])
def fetch_reviews(supplier_id):
    reviews = get_reviews(supplier_id)
    return jsonify(reviews), 200
