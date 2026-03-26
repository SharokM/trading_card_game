Suprhero Trading Card Web App 🎴

A full-stack Python + Flask web application to manage villain trading cards. Users can view, add, and delete villains, each with a name, description, interests, and image. The app is hosted live on Replit, requiring no setup to run.

🔗 Live Demo

Access the running app here:
Live on Replit - https://be5b015e-06bd-402f-b273-6f70823bd460-00-lu7qpv2wjsck.kirk.replit.dev/

Features
View Villains – Browse all villain cards.
Add Villains – Submit new villains with all details.
Delete Villains – Remove villains by name.
Database Tracking – Stores date added automatically.
Tech Stack
Python 3.12 🐍
Flask – Web framework
SQLite – Lightweight database
Gunicorn – Production-ready WSGI server
Replit – Hosting and live deployment
🚀 Running Locally (Optional)

To run the app locally for development:

Clone the repository:
git clone https://github.com/SharokM/trading_card_game.git
cd trading_card_game/trading_card_app
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Run the app using Gunicorn:
python -m gunicorn --bind 0.0.0.0:5000 app:app
Open your browser at http://localhost:5000.

Note: Local setup is optional. The Replit deployment runs the app fully without additional configuration.

Development & Contribution

Contributions are welcome! To contribute:

Fork the repository
Create a feature branch (git checkout -b feature/my-feature)
Commit your changes (git commit -m "Add my feature")
Push to the branch (git push origin feature/my-feature)
Create a Pull Request
Author

Sharok McDonnaugh – GitHub
