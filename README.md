# Bank API in Python

## Overview
This project is a RESTful API built using Django and Django REST Framework.
It exposes endpoints to fetch bank and branch details.

## Project Structure
```
├── src
│   ├── index.html
│   ├── index.js
│   ├── styles.css
│   └── assets
│       └── images
└── package.json
bankapi/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── bankapi/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── banks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   │   └── __init__.py
│   └── management/
│       └── commands/
│           └── load_csv.py
│
├── data/
│   └── bank_branches.csv
│
└── venv/
```

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (default)

## API Endpoints

### Get all banks
GET /api/banks/

### Get branches of a bank
GET /api/banks/{bank_id}/branches/

### Get branch details by IFSC
GET /api/branches/{ifsc}/

## Setup Instructions

1. Clone the repository
2. Create virtual environment
   python -m venv venv
3. Activate virtual environment
4. Run migrations
   python manage.py migrate
5. Start server
   python manage.py runserver

## Data Source
Bank and branch data was loaded from the provided dataset into the database.

## Time Taken
Approximately 4-5 hours.

## Notes
- Clean REST architecture followed
- Proper relational mapping between Bank and Branch models
