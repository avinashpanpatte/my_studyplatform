# Online Library with Python Backend and Database

This project is a Flask-based web application for an online library, integrated with a SQLite database using SQLAlchemy.

## Setup

1. Install Python (3.11 recommended).
2. Create virtual environment: `py -m venv venv`
3. Activate: `.\venv\Scripts\Activate.ps1`
4. Install dependencies: `pip install flask flask-sqlalchemy`
5. Run the app: `python app.py`
6. Populate database: `python populate.py`

## Features

- Flask web server
- SQLite database with Book model
- Templates for HTML pages
- Static CSS files

## Database Model

- Book: id, title, subject, description, link

The app serves the library pages and can store book data in the database.