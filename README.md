# Student Management System

A full-stack Student Management System built using **Python, Django, Django REST Framework, SQLite, HTML, CSS, and JavaScript**.

This project was developed as part of a **Python Full Stack Developer (Fresher) recruitment assessment**.

The application provides a web-based interface for managing student records with authentication, CRUD operations, search, validation, REST APIs, pagination, Django Admin, and automated testing.

---

## 📌 Project Overview

The Student Management System allows authenticated users to manage student information through a responsive web interface.

Users can:

- Login securely
- View all students
- Add new students
- Edit existing students
- Delete students with confirmation
- Search students by name or roll number
- Validate student information
- Manage students through Django Admin

The project also provides a REST API using Django REST Framework for programmatic student management.

---

## 🚀 Features

### 🔐 Authentication

- User login
- User logout
- Authentication-protected dashboard
- Django session-based authentication
- Protected REST API endpoints
- Django Admin authentication

### 👨‍🎓 Student Management

- View all students
- Add new students
- Edit existing students
- Delete students
- Delete confirmation
- Search students by name
- Search students by roll number
- Server-side form validation
- API-level validation

### 📋 Student Information

Each student record contains:

- Roll Number
- Student Name
- Email
- Mobile Number
- Course
- Year of Study
- Date of Admission

### 🌐 REST API

- Get all students
- Get student by ID
- Create student
- Update student
- Partially update student
- Delete student
- Search students
- Pagination
- Validation
- Error handling
- Authentication protection

### ⚙️ Django Admin

Administrators can:

- View students
- Add students
- Edit students
- Delete students
- Search students
- Filter students by course
- Filter students by year of study

### 🧪 Automated Testing

The project includes automated API tests covering:

- Student listing
- Student detail
- Student creation
- Student update
- Partial update
- Student deletion
- Student search
- Duplicate roll number validation
- Invalid mobile number validation
- Invalid year validation
- Non-existent student handling

---

# 🛠️ Tech Stack

## Backend

- Python 3.12+
- Django
- Django REST Framework

## Frontend

- HTML5
- CSS3
- JavaScript

## Database

- SQLite

## Authentication

- Django Authentication System
- Django Session Authentication

## Testing

- Django Test Framework
- Django REST Framework `APITestCase`

## Development Tools

- Git
- GitHub
- VS Code
- PowerShell

---

# 📂 Project Structure

```text
students-management-system/
│
├── student_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── student_form.html
│   │   └── student_confirm_delete.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_urls.py
│   ├── views.py
│   └── tests.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

# 💻 Installation & Setup

## Prerequisites

Make sure the following are installed:

- Python 3.12 or later
- Git
- Web browser
- VS Code or another code editor

---

## 1. Clone the Repository

Clone the project from GitHub:

```powershell
git clone https://github.com/SURENDAR-DHARMALINGAM/student-management-system.git
```

Navigate into the project:

```powershell
cd student-management-system
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv .venv
```

---

## 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

---

## 4. Install Dependencies

Install all required Python packages:

```powershell
python -m pip install -r requirements.txt
```

---

## 5. Apply Database Migrations

Create the database tables:

```powershell
python manage.py migrate
```

This will automatically create the SQLite database:

```text
db.sqlite3
```

The `db.sqlite3` file is excluded from Git using `.gitignore`.

---

## 6. Create a Superuser

Create an administrator account:

```powershell
python manage.py createsuperuser
```

Follow the prompts:

```text
Username:
Email address:
Password:
Password (again):
```

---

## 7. Run the Development Server

Start the Django development server:

```powershell
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

Open the URL in your browser.

---

# 🔑 Application URLs

## Login

```text
http://127.0.0.1:8000/login/
```

## Dashboard

```text
http://127.0.0.1:8000/
```

## Django Admin

```text
http://127.0.0.1:8000/admin/
```

## REST API

```text
http://127.0.0.1:8000/api/
```

---

# 🌐 REST API Documentation

The project uses **Django REST Framework** to provide RESTful APIs.

## Base URL

```text
http://127.0.0.1:8000/api/
```

## Student API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/students/` | Get all students |
| POST | `/api/students/` | Create a student |
| GET | `/api/students/<id>/` | Get student by ID |
| PUT | `/api/students/<id>/` | Update a student |
| PATCH | `/api/students/<id>/` | Partially update a student |
| DELETE | `/api/students/<id>/` | Delete a student |

---

# 🔎 Search API

Students can be searched using the `search` query parameter.

## Search by Student Name

```text
/api/students/?search=John
```

## Search by Roll Number

```text
/api/students/?search=STU001
```

The API searches both:

- Student Name
- Roll Number

---

# 📄 API Pagination

The API uses Django REST Framework page-number pagination.

The default page size is:

```text
10 students per page
```

Example:

```text
/api/students/?page=2
```

---

# 📝 Create Student API

## Request

```http
POST /api/students/
```

## Example JSON

```json
{
    "roll_number": "STU001",
    "student_name": "John Doe",
    "email": "john@example.com",
    "mobile_number": "9876543210",
    "course": "Computer Science",
    "year_of_study": 2,
    "date_of_admission": "2026-06-01"
}
```

## Successful Response

A successful student creation returns:

```text
HTTP 201 Created
```

---

# 🔄 Update Student API

## Full Update

```http
PUT /api/students/<id>/
```

## Partial Update

```http
PATCH /api/students/<id>/
```

Example:

```json
{
    "course": "Information Technology"
}
```

---

# 🗑️ Delete Student API

```http
DELETE /api/students/<id>/
```

A successful deletion returns an appropriate HTTP success response.

---

# ✅ Validation

The application performs validation at both the frontend form/server level and REST API level.

Validation includes:

- Roll number cannot be empty
- Roll number must be unique
- Student name cannot be empty
- Student name must contain at least 2 characters
- Email must be valid
- Email must be unique
- Mobile number must contain only digits
- Mobile number must contain exactly 10 digits
- Year of study must be between 1 and 6
- Admission date must be valid

Invalid requests return appropriate validation error responses.

---

# 🗄️ Database

The application uses **SQLite** as the default database.

Django migrations are used to create and manage database tables.

Run:

```powershell
python manage.py migrate
```

to create the database.

The local SQLite database file is:

```text
db.sqlite3
```

The database file is excluded from Git because it may contain local development data.

---

# ⚙️ Django Admin

The Django Admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials.

The admin panel provides:

- Student management
- Student search
- Course filtering
- Year-of-study filtering
- Add/Edit/Delete functionality

---

# 🧪 Testing

Run all automated tests with:

```powershell
python manage.py test
```

The current test suite contains:

```text
11 tests
```

The tests cover:

1. Student list
2. Student detail
3. Student creation
4. Student update
5. Partial update
6. Student deletion
7. Student search
8. Duplicate roll number validation
9. Invalid mobile number validation
10. Invalid year of study validation
11. Non-existent student handling

## Current Test Result

```text
Found 11 test(s).

...........

Ran 11 tests

OK
```

---

# 🔍 Django System Check

To verify the Django project configuration:

```powershell
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

---

# 🧰 Useful Django Commands

## Start Development Server

```powershell
python manage.py runserver
```

## Check Project Configuration

```powershell
python manage.py check
```

## Create Migrations

```powershell
python manage.py makemigrations
```

## Apply Migrations

```powershell
python manage.py migrate
```

## Run Tests

```powershell
python manage.py test
```

## Create Superuser

```powershell
python manage.py createsuperuser
```

---

# 🌿 Git Workflow

This project uses Git for version control.

Check project status:

```powershell
git status
```

Add changes:

```powershell
git add .
```

Create a commit:

```powershell
git commit -m "Add project documentation"
```

Push changes to GitHub:

```powershell
git push
```

---

# 📌 GitHub Repository

Repository:

```text
https://github.com/SURENDAR-DHARMALINGAM/student-management-system
```

---

# 🔮 Future Improvements

Possible future enhancements include:

- Bootstrap or Tailwind CSS integration
- Advanced student filtering
- Swagger/OpenAPI documentation
- Role-based permissions
- Docker deployment
- MySQL/PostgreSQL support
- Additional unit and integration tests
- Student profile pages
- CSV export
- PDF report generation
- Production deployment

---

# 📸 Screenshots

Screenshots of the following application pages can be added here:

### Login Page

_Add screenshot here._

### Student Dashboard

_Add screenshot here._

### Add Student

_Add screenshot here._

### Edit Student

_Add screenshot here._

### Delete Confirmation

_Add screenshot here._

### Django Admin

_Add screenshot here._

### REST API

_Add screenshot here._

---

# 👨‍💻 Author

**Surendar Dharmalingam**

Python Full Stack Developer — Fresher

---

# 📄 Project Purpose

This project was developed as part of a **Python Full Stack Developer recruitment assessment** to demonstrate practical knowledge of:

- Python
- Django
- Django REST Framework
- HTML
- CSS
- JavaScript
- SQLite
- CRUD operations
- Authentication
- REST APIs
- Data validation
- Error handling
- Automated testing
- Git and GitHub

---

# 📜 License

This project was developed for educational and recruitment assessment purposes.