from app import create_app
from api.inquiries_api import inquiries_bp
from api.reviews_api import reviews_bp

app = create_app()  # Create the Flask app using the factory function

# Register blueprints
app.register_blueprint(inquiries_bp, url_prefix="/api/inquiries")
app.register_blueprint(reviews_bp, url_prefix="/api/reviews")

if __name__ == "__main__":
    app.run(debug=True)
