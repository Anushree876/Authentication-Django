# Authentication Django Project 🔐🔐🔐

A Django web application implementing user registration, login, and profile management using SQLite as the database.
Frontend is built using Bootstrap.
---

## Features

- User signup and login functionality
- Custom user model and forms
- Password validation and authentication
- Admin interface
- Uses `django-bootstrap5` for styling forms and templates
- SQLite as the default database

---

## Getting Started

### Prerequisites

- Python 3.10+

---

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Anushree876/Authentication-Django.git
cd Authentication-Django

Install dependencies
pip install -r requirements.txt

Apply database migrations
python manage.py migrate

Create a superuser to access the admin panel
python manage.py createsuperuser

python manage.py runserver
Open your browser at http://127.0.0.1:8000
And get the authentication experience.
