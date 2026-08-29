# django_all_concepts
A comprehensive Django learning project covering Django concepts from beginner to advanced, with practical examples, authentication, ORM, forms, middleware, signals, testing, and more.


A comprehensive **Django learning and reference project** covering Django concepts from beginner to advanced.

This project is created to learn, practice, and demonstrate important Django concepts through practical examples and implementations.

---

## 📚 About This Project

**django_all_concepts** is a hands-on Django project that covers the major concepts used in real-world Django development.

The goal is to maintain one project where Django concepts can be learned and practiced step by step.

Topics will be added progressively as the project grows.

---

## 🛠️ Technologies

* Python
* Django
* SQLite / MySQL
* HTML5
* CSS3
* Bootstrap
* JavaScript
* Git & GitHub

---

## 📖 Django Concepts Covered

### 1. Django Basics

* Creating a Django project
* Creating Django applications
* Project structure
* Application structure
* `manage.py`
* `settings.py`
* `urls.py`
* `views.py`
* `models.py`
* `admin.py`
* `apps.py`
* URL routing
* Views
* Templates
* Static files
* Media files

### 2. Templates

* Django Template Language (DTL)
* Template variables
* Template tags
* Template filters
* Template inheritance
* `{% extends %}`
* `{% block %}`
* `{% include %}`
* Template loops
* Conditional statements
* Custom template tags
* Custom template filters

### 3. Models & ORM

* Creating models
* Model fields
* Primary keys
* Relationships

  * One-to-One
  * One-to-Many
  * Many-to-Many
* Model Meta
* Model methods
* Model managers
* QuerySets
* Filtering
* Ordering
* Aggregation
* Annotation
* `select_related()`
* `prefetch_related()`
* Transactions
* Database migrations

### 4. Django Admin

* Registering models
* Customizing admin
* `ModelAdmin`
* List display
* Search
* Filters
* Ordering
* Custom admin actions
* Inline models

### 5. Forms

* Django Forms
* ModelForms
* Form validation
* Custom validation
* Form widgets
* Form fields
* Handling form submission
* File uploads

### 6. Authentication & Authorization

* User authentication
* Login
* Logout
* Registration
* Password management
* Groups
* Permissions
* Custom user model
* Authentication backends
* Login required
* User authorization

### 7. Class-Based Views

* Function-Based Views
* Class-Based Views
* `TemplateView`
* `ListView`
* `DetailView`
* `CreateView`
* `UpdateView`
* `DeleteView`
* Mixins

### 8. Middleware

* Django middleware
* Custom middleware
* Request processing
* Response processing
* Middleware execution order

### 9. Sessions & Cookies

* Django sessions
* Cookies
* Session management
* Session authentication
* Session-based data

### 10. Django Messages

* Success messages
* Error messages
* Warning messages
* Info messages
* Debug messages

### 11. Signals

* Django signals
* `pre_save`
* `post_save`
* `pre_delete`
* `post_delete`
* Custom signals

### 12. File Handling

* File uploads
* Image uploads
* `MEDIA_ROOT`
* `MEDIA_URL`
* Static files
* `STATIC_ROOT`
* `STATIC_URL`

### 13. Django REST Framework

* REST APIs
* Serializers
* Model Serializers
* APIView
* Generic Views
* Mixins
* ViewSets
* ModelViewSet
* Routers
* Authentication
* Permissions
* Pagination
* Filtering
* Searching
* Ordering
* API validation
* JWT authentication

### 14. API Authentication

* Token Authentication
* JWT Authentication
* Access tokens
* Refresh tokens
* Protected APIs
* API permissions

### 15. Advanced Django

* Custom managers
* Custom middleware
* Custom commands
* Context processors
* Decorators
* Signals
* Transactions
* Database optimization
* Caching
* Logging
* Internationalization
* Localization
* Django security
* Django testing

### 16. Testing

* Unit testing
* Django TestCase
* Test client
* Model testing
* View testing
* Form testing
* API testing

### 17. Deployment

* Production settings
* Environment variables
* PostgreSQL/MySQL
* Gunicorn
* Static files
* Media files
* Security settings
* Deployment configuration

---

## 📁 Project Structure

The project will be organized into separate Django applications based on concepts.

```text
django_all_concepts/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── basics/
├── templates_demo/
├── models_demo/
├── forms_demo/
├── authentication/
├── class_based_views/
├── middleware_demo/
├── sessions_demo/
├── signals_demo/
├── file_handling/
├── api/
├── authentication_api/
└── testing/
```

> The application structure may change as new Django concepts are added.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/django_all_concepts.git
```

### 2. Navigate to the project

```bash
cd django_all_concepts
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows CMD:

```bash
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Environment Variables

Sensitive information should not be stored directly in the repository.

Example:

```text
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=database_name
DATABASE_USER=database_user
DATABASE_PASSWORD=database_password
```

Use a `.env` file for local development and keep it out of Git.

---

## 🧪 Running Tests

Run Django tests using:

```bash
python manage.py test
```

---

## 🎯 Project Goals

The main goals of this project are:

* Learn Django from beginner to advanced level
* Understand Django architecture
* Practice Django ORM
* Build database-driven applications
* Learn authentication and authorization
* Build REST APIs using Django REST Framework
* Understand Django security
* Learn Django testing
* Practice real-world Django development
* Maintain a reusable Django reference project

---

## 🚀 Future Improvements

The project will continue to expand with additional concepts such as:

* Advanced ORM optimization
* Caching
* Celery
* Redis
* WebSockets
* Django Channels
* Docker
* PostgreSQL
* API documentation
* Automated testing
* CI/CD
* Production deployment

---

## 📌 Learning Approach

Each concept should contain:

1. Concept explanation
2. Django implementation
3. Example code
4. Database example where applicable
5. API example where applicable
6. Practical use case

This makes the repository useful as both a **learning project and a future Django reference**.

---

## 🤝 Contribution

This is primarily a personal learning and reference project, but suggestions and improvements are welcome.

---

## 📄 License

This project is created for learning and educational purposes.
