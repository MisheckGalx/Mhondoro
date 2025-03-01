from models import Review, db

def create_review(user_id, data):
    try:
        review = Review(
            miner_id=user_id,
            supplier_id=data["supplier_id"],
            rating=data["rating"],
            comment=data["comment"]
        )
        db.session.add(review)
        db.session.commit()
        return {"message": "Review added successfully", "status": 201}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e), "status": 400}

def get_reviews(supplier_id):
    reviews = Review.query.filter_by(supplier_id=supplier_id).all()
    return [{"id": r.id, "rating": r.rating, "comment": r.comment} for r in reviews]
