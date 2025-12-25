# BankInfo_API



# Bank API in Python

## Overview
This project is a RESTful API built using Django and Django REST Framework.
It exposes endpoints to fetch bank and branch details.

## Project Structure
bankapi/
├── bankapi/                  # Main Django project configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # Root URL configuration
│   ├── asgi.py               # ASGI config
│   └── wsgi.py               # WSGI config
│
├── banks/                    # Django app handling bank & branch logic
│   ├── management/
│   │   └── commands/
│   │       └── load_csv.py   # Custom management command to load CSV data
│   ├── migrations/           # Database migrations
│   ├── models.py             # Bank and Branch models
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views
│   ├── urls.py               # App-level API routes
│   └── admin.py              # Admin configuration
│
├── data/
│   └── bank_branches.csv     # Dataset used to populate the database
│
├── db.sqlite3                # SQLite database (local development)
├── manage.py                 # Django management entry point
└── venv/                     # Python virtual environment


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
