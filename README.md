# BankInfo_API



# Bank API in Python

## Overview
This project is a RESTful API built using Django and Django REST Framework.
It exposes endpoints to fetch bank and branch details.

#Project Structure
bankapi/
├── bankapi/                  # Django project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── banks/                    # Django app
│   ├── management/
│   │   └── commands/
│   │       └── load_csv.py   # Custom command
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── data/
│   └── bank_branches.csv     # Dataset
│
├── db.sqlite3
├── manage.py
└── venv/


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
4. Install dependencies
   pip install -r requirements.txt
5. Run migrations
   python manage.py migrate
6. Start server
   python manage.py runserver

## Data Source
Bank and branch data was loaded from the provided dataset into the database.

## Time Taken
Approximately 4-5 hours.

## Notes
- Clean REST architecture followed
- Proper relational mapping between Bank and Branch models
