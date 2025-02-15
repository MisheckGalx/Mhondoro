admin_api = Blueprint('admin_api', __name__)

# Admin route to delete user
@admin_api.route('/admin/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200

# Admin route to delete equipment
@admin_api.route('/admin/equipment/<int:id>', methods=['DELETE'])
def delete_equipment_admin(id):
    equipment = Equipment.query.get(id)
    if not equipment:
        return jsonify({"message": "Equipment not found"}), 404

    db.session.delete(equipment)
    db.session.commit()

    return jsonify({"message": "Equipment deleted successfully"}), 200
