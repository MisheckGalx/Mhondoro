from app.models import Inquiry, db

def create_inquiry(user_id, data):
    try:
        inquiry = Inquiry(
            miner_id=user_id,
            supplier_id=data["supplier_id"],
            equipment_id=data["equipment_id"],
            message=data["message"]
        )
        db.session.add(inquiry)
        db.session.commit()
        return {"message": "Inquiry sent successfully", "status": 201}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e), "status": 400}

def get_inquiries(user_id):
    inquiries = Inquiry.query.filter_by(supplier_id=user_id).all()
    return [{"id": i.id, "miner_id": i.miner_id, "message": i.message} for i in inquiries]
