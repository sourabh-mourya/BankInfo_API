# Bank API in Python

## Overview
This project is a RESTful API built using Django and Django REST Framework.
It exposes endpoints to fetch bank and branch details.

## 📁 Project Structure
```
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
## 📂 Directory & File Explanation

* `manage.py` :-  Django command-line utility used to run the development server, apply migrations, and execute custom management commands.
* `db.sqlite3` :-   SQLite database used for local development and testing.
* `requirements.txt` :-   Contains all Python dependencies required to run the project.
* `bankapi/` :-   Main Django project configuration directory.
* `settings.py` :- Global project settings and configurations
* `urls.py` :- Root URL routing for the project
* `asgi.py / wsgi.py` :- Deployment configuration files
* `banks/` :-   Django application responsible for bank and branch-related logic.
* `models.py` – Bank and Branch database models
* `serializers.py` :- Django REST Framework serializers
* `views.py` :- API logic and request handling
* `urls.py` :- App-level API routes
* `admin.py` :- Django admin panel configuration
* `management/commands/load_csv.py` :-Custom Django command to load bank and branch data from CSV
* `data/` :-   Contains the CSV dataset used to populate the database.
* `venv/` :-  Python virtual environment used only for local development (not included in version control).

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (default)

### 🔗 API ENDPOINTS


## Get All Banks
   GET /api/banks/
   Response Example
   
           {
             "id": 1,
             "name": "STATE BANK OF INDIA"
           }
      

## Get Branches of a Bank
   GET /api/banks/{bank_id}/branches/
   Response Example
   
           {
                "ifsc": "SBIN0000001",
                "branch": "MAIN BRANCH",
           }
      

## Get Branch Details by IFSC
   GET /api/branches/{ifsc}/
   Response Example

      {
           "ifsc": "SBIN0000001",
           "branch": "MAIN BRANCH",
           "bank": "STATE BANK OF INDIA",
           "city": "MUMBAI",
           "state": "MAHARASHTRA",
           "address": "Mumbai Main Branch"
      }

      
### ⚙️ How to Run the Project
1.Clone the repository
   git clone <repository-url>
   cd bankapi
2.Create a virtual environment
   python -m venv venv
3.Activate the virtual environment
   Windows:
      venv\Scripts\activate
   Linux / macOS:
      source venv/bin/activate
3.Install dependencies
   pip install -r requirements.txt
4.Apply database migrations
   python manage.py migrate
5.Load bank and branch data from CSV
   python manage.py load_csv
6.Run the development server
   python manage.py runserver
8.Access the APIs
   GET /api/banks/
   GET /api/banks/{bank_id}/branches/
   GET /api/branches/{ifsc}/
   
## 📊 Data Source
Bank and branch data is loaded from a CSV file (bank_branches.csv) using a custom Django management command.

## ⏱ Time Taken
Approximately 4–5 hours.


### Why Django + Django REST Framework Was Chosen

Django was chosen because it provides a robust, secure, and scalable backend framework with built-in support for ORM, migrations, and admin tooling, which makes managing relational data like banks and branches straightforward.
Django REST Framework (DRF) was selected to implement RESTful APIs efficiently. DRF offers:
      - Clean and structured API development
      - Powerful serializers for converting model data to JSON
      -  Generic views that reduce boilerplate code
      - Built-in support for REST best practices

Using Django with DRF ensures:
  - Maintainable and readable code
  - Proper separation of concerns
  -Fast development while adhering to industry standards

This stack is well-suited for building production-grade REST APIs and aligns perfectly with the requirements of the assignment.


## Notes
- Clean REST architecture followed
- Proper relational mapping between Bank and Branch models
