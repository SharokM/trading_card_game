🎴 Villain Trading Card Web App

A full-stack Flask web application for managing a collection of villain trading cards.
Users can create, view, and delete villains, each with associated metadata and imagery.

The application is deployed publicly using a production-ready setup with Gunicorn and Railway.

🌐 Live Demo URL:
https://tradingcardgame-production.up.railway.app/

✨ Features
View Villains — Browse all stored villain cards
Add Villains — Create new entries with name, description, interests, and image URL
Delete Villains — Remove villains by name
REST API — JSON endpoints for retrieving and modifying data
Automatic Timestamps — Tracks when each villain is added


🏗️ Architecture Overview
This project follows a simple full-stack architecture:
Backend: Flask (Python)
Database: SQLite via SQLAlchemy ORM
Server: Gunicorn (WSGI production server)
Hosting: Railway (container-based deployment)


      Client 
        ↓
      Flask 
        ↓
    SQLAlchemy
        ↓
     SQLite

     
📦 Tech Stack
Python 3.x
Flask
Flask-SQLAlchemy
Gunicorn
SQLite
Railway (deployment)


🚀 Deployment
The application is deployed on Railway using a production WSGI server:
gunicorn app:app

Notes:
The app runs inside a containerized environment
SQLite is used for simplicity, but data is ephemeral on Railway free tier

🛠️ Running Locally
1. Clone the repository
git clone https://github.com/<your-username>/trading_card_app.git
cd trading_card_app

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
Development server:
python app.py

Production-style (recommended):
gunicorn app:app


🔌 API Endpoints
Get all villains
GET /api/villains/
Add a villain
POST /api/villains/add
Delete a villain
POST /api/villains/delete

⚠️ Known Limitations
SQLite database may reset on redeploy (Railway free tier)
No authentication or user management
No input validation beyond basic checks

🔮 Future Improvements
Migrate to PostgreSQL for persistent storage
Add authentication (user accounts)
Improve UI/UX and styling
Add update/edit functionality
Pagination and search

👤 Author
Sharok McDonnaugh
