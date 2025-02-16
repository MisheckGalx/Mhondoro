# Mhondoro - Mining Equipment Directory 🚜

## 📌 Overview
Mhondoro is a web-based platform that connects small-scale miners in Zimbabwe with suppliers offering mining equipment for sale or rent. The platform provides a structured way to browse, compare, and contact suppliers efficiently.

## 🔍 Features
- **Equipment Listings:** Suppliers can add, edit, and remove listings.
- **Search & Filters:** Miners can find equipment based on type, location, and price.
- **User Authentication:** Separate accounts for suppliers and miners.
- **Contact System:** Miners can send inquiries and chat with suppliers.
- **Reviews & Ratings:** Miners can rate suppliers to build trust.
- **Responsive Design:** Mobile-friendly UI for easy access.

## 🛠 Tech Stack
### Backend:
- **Flask (Python)** - API and business logic.
- **PostgreSQL/MySQL** - Database for storing users, equipment, and messages.
- **SQLAlchemy** - ORM for database interactions.

### Frontend:
- **React.js** - Modern and interactive UI.
- **Tailwind CSS** - Responsive styling.
- **Leaflet.js / Google Maps API** - Location-based search.

### Deployment:
- **Backend:** Hosted on Heroku/DigitalOcean/AWS EC2.
- **Frontend:** Deployed via Vercel/Netlify.
- **Database:** Hosted on Supabase/PlanetScale/AWS RDS.

## 🚀 Installation Guide
### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/MisheckGalx/Mhondoro.git
 cd Mhondoro
```

### 2️⃣ Set Up the Backend (Flask)
#### Create a Virtual Environment & Install Dependencies
```sh
 python3 -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
 pip install -r requirements.txt
```

#### Configure Database
Update `.env` with your database credentials:
```sh
 DATABASE_URL=postgresql://user:password@localhost/mhondoro
```

#### Run Migrations & Start Server
```sh
 flask db upgrade
 flask run
```

### 3️⃣ Set Up the Frontend (React)
```sh
 cd frontend
 npm install
 npm start
```

## 📌 API Endpoints
### Authentication
- **POST** `/auth/register` → User registration
- **POST** `/auth/login` → User login

### Equipment Listings
- **GET** `/equipment` → Fetch all equipment
- **POST** `/equipment` → Add new listing (Suppliers only)
- **PUT** `/equipment/:id` → Update listing
- **DELETE** `/equipment/:id` → Remove listing

### Inquiries & Reviews
- **POST** `/inquiries` → Send an inquiry
- **POST** `/reviews` → Leave a supplier review

## 📅 Development Timeline
| Week  | Task |
|-------|-------------------------------|
| Week 1 | Set up project structure & DB |
| Week 2 | Build UI, authentication, CRUD |
| Week 3 | Add messaging, reviews, UX tweaks |
| Week 4 | Testing, bug fixes, deployment |

## 💰 Monetization Strategies
- **Featured Listings:** Suppliers pay for priority visibility.
- **Transaction Fee:** A percentage on rentals.
- **Advertisements:** Mining companies can advertise their services.

## 👥 Contributors
- **Misheck Gogo** - Lead Developer

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
🚀 **Let's make Mhondoro the best mining equipment directory in Zimbabwe!**
