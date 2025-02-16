import jwt
from datetime import datetime, timedelta
from flask_mail import Message
from app import app, mail


# Utility function to encode authentication token
def encode_auth_token(user_id):
    """Generates an authentication token for the user."""
    try:
        # Set the token expiration time (1 day)
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),  # Token expiration time
            'iat': datetime.utcnow(),  # Token issued time
            'sub': user_id  # Subject of the token (user ID)
        }
        # Encode the token using the secret key
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    except Exception as e:
        # Return the error message if something goes wrong
        return str(e)


# Utility function to decode authentication token
def decode_auth_token(auth_token):
    """Decodes the authentication token and returns the user ID."""
    try:
        # Decode the token using the secret key
        payload = jwt.decode(auth_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']  # Return the user ID (subject) from the payload
    except jwt.ExpiredSignatureError:
        # Return a message if the token is expired
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        # Return a message if the token is invalid
        return 'Invalid token. Please log in again.'


# Function to send email
def send_email(subject, recipient, body):
    """Sends an email using Flask-Mail."""
    try:
        # Create the message object
        msg = Message(subject, recipients=[recipient])
        msg.body = body  # Set the body of the email
        # Send the email using Flask-Mail
        mail.send(msg)
        return "Email sent successfully!"
    except Exception as e:
        # Return the error message if something goes wrong
        return f"Error sending email: {str(e)}"
