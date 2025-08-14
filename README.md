# Django Authentication Project Setup Guide

This guide will help you clone, install, and run the Django authentication project locally using SQLite.

---

## 🚀 Step-by-Step Setup Instructions

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Anushree876/Authentication-Django.git
cd Authentication-Django

2. Install Required Python Packages
Install all dependencies listed in requirements.txt:
pip install -r requirements.txt

3. Apply Migrations
Run the following commands to set up your database:
python manage.py makemigrations
python manage.py migrate
✅ This will create the default db.sqlite3 database file.

4. Create a Superuser for Admin Access
python manage.py createsuperuser
You'll be prompted to enter a username, email, and password.

5. Run the Development Server
python manage.py runserver
Once the server starts, visit the following URLs in your browser:

🌐 Homepage: http://127.0.0.1:8000/

🔐 Admin Panel: http://127.0.0.1:8000/admin/



