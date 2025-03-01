from flask import Blueprint, request, jsonify
from app.services.inquiry_service import create_inquiry, get_inquiries
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Inquiry, db

inquiries_bp = Blueprint("inquiries", __name__)

@inquiries_bp.route("/", methods=["POST"])
@jwt_required()
def send_inquiry():
    data = request.get_json()
    user_id = get_jwt_identity()
    response = create_inquiry(user_id, data)
    return jsonify(response), response.get("status", 400)

@inquiries_bp.route("/", methods=["GET"])
@jwt_required()
def fetch_inquiries():
    user_id = get_jwt_identity()
    inquiries = get_inquiries(user_id)
    return jsonify(inquiries), 200
