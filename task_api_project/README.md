Task Management API
A secure and scalable RESTful API for managing user-specific tasks.
Built with Django and Django REST Framework, the API provides authentication, task ownership enforcement, and full task lifecycle management.

📌 Overview

The Task Management API allows users to:
Register and authenticate securely
Create, view, update, and delete personal tasks
Mark tasks as completed or incomplete
Access only their own data through token-based authentication
The system is designed following REST best practices and enforces strict user-level data isolation.

✨ Features
Token-based user authentication
User profile endpoint (/users/me)
Full CRUD operations for tasks
Task completion state management
Secure user-task ownership enforcement
Django Admin support for management
Clean and modular project structure

🛠 Tech Stack
Python
Django
Django REST Framework
DRF Token Authentication
SQLite (development database)

🔐 Authentication
Authentication is handled using DRF Token Authentication.
After registration or login, users receive a token
This token must be included in the Authorization header for protected endpoints

📡 API Endpoints

Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Authenticate user and return token
POST	/api/auth/logout/	Logout user (invalidate token)

User
Method	Endpoint	Description
GET	/api/users/me/	Retrieve logged-in user information

Tasks
Method	Endpoint	Description
GET	/api/tasks/	List all tasks for authenticated user
POST	/api/tasks/	Create a new task
GET	/api/tasks/<id>/	Retrieve a single task
PUT	/api/tasks/<id>/	Update a task
DELETE	/api/tasks/<id>/	Delete a task
PATCH	/api/tasks/<id>/complete/	Mark task as completed
PATCH	/api/tasks/<id>/incomplete/	Mark task as incomplete

🧱 Data Model (ERD Summary)

User
id
username
email
password (hashed)
date_joined

Task
id
title
description
is_completed
created_at
updated_at
user (Foreign Key → User)
Relationship:
One User → Many Tasks