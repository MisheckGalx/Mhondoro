# app/services/review_service.py

from app.models import Review, db  # Ensure the Review model and db are imported

def create_review(user_id, data):
    try:
        new_review = Review(
            user_id=user_id,
            equipment_id=data['equipment_id'],
            rating=data['rating'],
            comment=data.get('comment', '')
        )
        db.session.add(new_review)
        db.session.commit()
        return {"message": "Review created successfully", "status": 201}
    except Exception as e:
        return {"message": str(e), "status": 400}

def get_reviews(user_id):
    try:
        reviews = Review.query.filter_by(user_id=user_id).all()
        return [review.to_dict() for review in reviews]  # Assuming `to_dict` method exists on your Review model
    except Exception as e:
        return {"message": str(e), "status": 400}
