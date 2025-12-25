# Bank API in Python

## Overview
This project is a RESTful API built using Django and Django REST Framework.
It exposes endpoints to fetch bank and branch details.

## Project Structure
bankapi/
│
├── manage.py                     # Django management entry point
├── db.sqlite3                    # SQLite database
├── requirements.txt              # Project dependencies
│
├── bankapi/                      # Django project configuration
│   ├── __init__.py
│   ├── settings.py               # Global settings
│   ├── urls.py                   # Root URL configuration
│   ├── asgi.py                   # ASGI config
│   └── wsgi.py                   # WSGI config
│
├── banks/                        # Django app (Banks & Branches)
│   ├── __init__.py
│   ├── admin.py                  # Admin registrations
│   ├── apps.py                   # App config
│   ├── models.py                 # Bank & Branch models
│   ├── serializers.py            # DRF serializers
│   ├── views.py                  # API views
│   ├── urls.py                   # App-level routes
│   ├── migrations/               # Database migrations
│   │   └── __init__.py
│   └── management/
│       └── commands/
│           └── load_csv.py        # Custom CSV loader command
│
├── data/
│   └── bank_branches.csv         # CSV dataset
│
└── venv/                         # Virtual environment (local only)

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
