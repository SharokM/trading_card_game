Superhero Trading Card Game

Superhero Trading Card Game is a full-stack web application that displays superhero and villain trading cards. Users can view cards, add new cards, and delete existing cards through a simple web interface.
The project uses a Python Flask backend with a SQLite database and a front-end built with HTML, CSS, JavaScript, and jQuery.

What This App Does
Displays superhero / villain trading cards
Shows character name, description, interests, image, and date added
Allows users to add new cards using a form
Allows users to delete cards by name
Stores all card data in a SQLite database
Uses API endpoints to communicate between frontend and backend

Technologies Used
Python
Flask
SQLite
SQLAlchemy
HTML5
CSS3
JavaScript
jQuery

Project Files
app.py – Flask server, database models, and API routes
villain.html – displays all trading cards
addvillain.html – form to add a new card
deletevillain.html – form to delete a card
static/villain.js – fetches and displays cards
static/addvillain.js – handles adding cards
static/delete.js – handles deleting cards
static/villain.css – styling

Requirements
To run this project, you need:
Python 3
pip
A modern web browser
Database Information
Uses SQLite (villain.db)

Database is created automatically when the app runs

Stores:
name
description
interests
image URL
date added

API Routes
GET /api/villains/
Returns all villains as JSON

POST /api/villains/add
Adds a new villain to the database

POST /api/villains/delete
Deletes a villain by name

How To Run The App
Install dependencies
pip install flask flask_sqlalchemy

Run the server
python app.py

Open in browser
http://localhost:8080

Notes
This is a full-stack project
No authentication or user accounts
Form validation is handled on the backend
Images are loaded using external URLs


S McDonnaugh
Superhero Trading Card Game
