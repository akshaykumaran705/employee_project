#  Employee Management System API

This is a backend application built using **Django** and **Django REST Framework** that provides RESTful APIs for managing employee data, departments, attendance, and performance metrics. The system is designed to be scalable, secure, and extensible with support for authentication, pagination, filtering, and more.

---

##  Project Overview

This Employee Management System allows organizations to track and manage their workforce efficiently through REST APIs. It is ideal for HR teams and administrators who need tools for:

- Registering and updating employee details
- Managing department assignments
- Tracking employee attendance
- Recording and analyzing performance reviews

The backend is powered by:

- **Django 4.x**
- **Django REST Framework**
- **PostgreSQL** for data persistence
- **Token or JWT-based Authentication**
- Optional: Docker support for containerized deployment

---

##  Setup Instructions

###  Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.10 or higher
- PostgreSQL
- Git
- Virtualenv (recommended)

---

###  Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/akshaykumaran705/employee_project.git
cd employee_project
```

---

#### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

#### 3. Install Required Python Packages

```bash
pip install -r requirements.txt
```

---

#### 4. Configure PostgreSQL Database

Create a PostgreSQL database manually using your preferred tool (e.g., `psql`, pgAdmin).

Update the `DATABASES` setting in `employee_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

#### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

#### 6. Create Superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

---

#### 7. Run the Development Server

```bash
python manage.py runserver
```

The server will be available at:  
[http://localhost:8000/](http://localhost:8000/)

Visit: [http://localhost:8000/admin](http://localhost:8000/admin) to access the Django admin dashboard.

---

##  Authentication Guide

This project supports:

- **Token Authentication**
- **JWT Authentication** (if enabled)

To obtain a JWT token:

```http
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
```

Use the access token in the `Authorization` header for API requests:

```http
Authorization: Bearer <your_token>
```

---

## 📡 API Usage Guide

The API is structured into four main modules: Employees, Departments, Attendance, and Performance.

All endpoints are prefixed with `/api/`.

---

###  Employees

| Method | Endpoint                | Description                       |
|--------|-------------------------|-----------------------------------|
| GET    | `/api/employees/`       | List all employees                |
| POST   | `/api/employees/`       | Create a new employee             |
| GET    | `/api/employees/{id}/`  | Retrieve details of one employee |
| PUT    | `/api/employees/{id}/`  | Update employee data              |
| DELETE | `/api/employees/{id}/`  | Delete an employee                |

**Example: Create a new employee**

```http
POST /api/employees/
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "department": 2,
  "position": "Data Analyst"
}
```

---

###  Departments

| Method | Endpoint                  | Description                    |
|--------|---------------------------|--------------------------------|
| GET    | `/api/departments/`       | List all departments           |
| POST   | `/api/departments/`       | Create a new department        |
| GET    | `/api/departments/{id}/`  | View details of a department   |
| PUT    | `/api/departments/{id}/`  | Update department info         |
| DELETE | `/api/departments/{id}/`  | Delete a department            |

---

###  Attendance

| Method | Endpoint                | Description                         |
|--------|-------------------------|-------------------------------------|
| GET    | `/api/attendance/`      | List all attendance records         |
| POST   | `/api/attendance/`      | Add attendance for an employee      |

**Example: Add attendance**

```http
POST /api/attendance/
{
  "employee": 3,
  "date": "2025-06-18",
  "status": "Present"
}
```

---

###  Performance

| Method | Endpoint                  | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/api/performance/`       | List performance reviews        |
| POST   | `/api/performance/`       | Add a performance review        |

**Example: Submit performance review**

```http
POST /api/performance/
{
  "employee": 4,
  "review_period": "Q2 2025",
  "score": 85,
  "comments": "Consistently meets expectations."
}
```

---

##  Filtering, Search, and Pagination

- Filter by field:  
  `/api/employees/?department=2`

- Search by name/email (if enabled):  
  `/api/employees/?search=John`

- Paginate results:  
  `/api/employees/?page=2`

---

##  Swagger Documentation (Optional)

If Swagger is set up using `drf-yasg`, access:

```http
http://localhost:8000/swagger/
```

Or Redoc:

```http
http://localhost:8000/redoc/
```

---

##  Docker Setup (Optional)

If Docker support is enabled:

```bash
docker-compose up --build
```

Make sure to:

- Create a `.env` file with your secrets
- Ensure ports and volumes are mapped correctly in `docker-compose.yml`

---

##  Folder Structure Overview

```
employee_project/
├── api/                  # Django app for business logic
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── employee_project/     # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── Dockerfile (optional)
├── docker-compose.yml (optional)
└── README.md
```
---

##  Contact

For questions, suggestions, or collaboration:

- GitHub: [@akshaykumaran705](https://github.com/akshaykumaran705)
- LinkedIn: [Akshay Kumaran Venkatesan](https://www.linkedin.com/in/akshay-kumaran-venkatesan-a179b5112/)
