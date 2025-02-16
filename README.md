# Mhondoro - Mining Equipment & Service Directory

**Mhondoro** is a comprehensive, user-friendly platform designed to connect mining professionals in Zimbabwe with equipment and service providers. Whether you're looking for mining equipment or services, **Mhondoro** offers a streamlined experience for discovering, reviewing, and purchasing mining machinery and related services.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

---

## Overview

**Mhondoro** is a directory app aimed at the mining industry, providing a platform for mining equipment and service providers to list their products and services. It offers detailed listings of equipment, including specifications, availability, and contact information. Users can review equipment and services, creating a transparent environment for business transactions. The backend is built using **Flask**, with JWT-based authentication, a RESTful API for integration, and secure file upload functionality for equipment images.

---

## Features

- **User Registration & Login**: Secure user registration and login using JWT (JSON Web Tokens).
- **Directory of Mining Equipment**: Browse and search for mining equipment by category, location, or specifications.
- **Image Uploads for Equipment**: Equipment owners can upload images of their products to make listings more attractive.
- **Pagination**: Efficient pagination for long lists of equipment and reviews.
- **Reviews & Ratings**: Users can leave reviews and ratings for equipment and services.
- **Admin Panel**: Admin users can manage listings, users, and reviews.
- **RESTful API**: Exposes endpoints to interact with the data programmatically.
- **Email Notifications**: Users receive email notifications on registration and important updates.

---

## Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL / SQLite (development)
- **Authentication**: JWT (JSON Web Tokens)
- **File Uploads**: Flask-Uploads for managing images
- **Testing**: Unittest
- **Email Service**: Flask-Mail for user notifications
- **API Documentation**: OpenAPI (optional)

---

## Installation

To get started with **Mhondoro**, follow the steps below to clone the repository and set up the development environment.

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- **PostgreSQL**: Install PostgreSQL or use SQLite for local development.

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/mhondoro.git
   cd mhondoro

2. **Create and activate a virtual environment**:

   python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**:

    pip install -r requirements.txt

4. **Set up environment variables**:
Create a .env file in the root directory and configure it with the following values:

    FLASK_APP=run.py
    FLASK_ENV=development
    SECRET_KEY=your-secret-key
    DATABASE_URL=your-database-url  # Example: postgres://user:password@localhost/mhondoro

5. **Run database migrations**:
    flask db upgrade

6. **Start the development server**:
    flask run

7. **Access the app**:
    Visit http://127.0.0.1:5000 in your browser.
Usage
Once the app is running, you can interact with the platform through the following routes:

User Registration & Authentication
POST /register: Register a new user.
POST /login: Login and receive a JWT token for authentication.
Equipment Directory
GET /equipment: View all equipment (supports pagination).
GET /equipment/<id>: View details of a specific equipment.
POST /equipment: Add new equipment (admin only).
PUT /equipment/<id>: Update an equipment listing (admin only).
DELETE /equipment/<id>: Delete an equipment listing (admin only).
Reviews
POST /reviews: Add a review for an equipment item.
GET /reviews/<equipment_id>: Get reviews for an equipment item.
Admin Panel (Admin-only routes)
GET /admin/equipment: List all equipment in the directory.
GET /admin/users: List all registered users.
Contributing
We welcome contributions from the community! If you have suggestions, improvements, or bug fixes, feel free to create a pull request or report an issue.

Steps to Contribute:
Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes and commit them (git commit -m 'Add new feature')
Push to your fork (git push origin feature-branch)
Open a pull request for review
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask: For being a lightweight and powerful web framework.
SQLAlchemy: For object-relational mapping and database integration.
Flask-Mail: For handling email notifications.
Flask-Uploads: For easy file management and uploads.
JWT: For securing the app with token-based authentication.
PostgreSQL: For the database management system.




---

You can copy this code directly into your `README.md` file. It provides an excellent structure and clear instructions, ensuring users can easily set up, use, and contribute to the **Mhondoro** project. Let me know if you need any adjustments or further details.
