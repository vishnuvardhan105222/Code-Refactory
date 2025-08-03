##User Management API — Refactoring Summary

Overview

This project is a refactored version of a legacy User Management API built with Flask and SQLite. The original code worked but had significant issues related to security, maintainability, and best practices.

This Changes.md file explains the key changes made during the refactor to improve the overall quality and reliability of the application.

## In This What are the Changes I have done and Why it is ?

### 1. **Code Organization and Structure**
-> Split database connection logic into a separate `db.py` module with a reusable `get_db_connection()` function.
-> Wrapped database initialization into a dedicated `initialize_db()` function, improving reusability and separation of concerns.
-> Ensured all files (`app.py`, `db.py`) are modular and easy to maintain.

### 2. **Security Improvements**
-> Replaced raw SQL query string concatenation with **parameterized queries** (`?` placeholders) to prevent SQL injection attacks.
-> Planned password hashing using Werkzeug’s `generate_password_hash` and `check_password_hash` (not fully implemented yet but structured for easy addition).
-> Enforced **unique constraint** on user emails to avoid duplicates and improve data integrity.

### 3. **Error Handling and API Responses**
-> Added **try-except blocks** around database operations to catch and respond gracefully to unexpected errors.
-> Returned appropriate HTTP status codes (e.g., `200` for success, `201` for resource creation, `400` for bad requests, `404` when users not found).
-> Responses are now consistently in JSON format for easier client-side consumption.

### 4. **Data Validation and Consistency**
-> Validated required fields (`name`, `email`, `password`) on user creation and update endpoints.
-> Added checks to prevent insertion of duplicate users during database initialization.
-> Handled missing query parameters and invalid input gracefully.

### 5. **Database Initialization**
- Created a robust `init_db.py` script that creates the `users` table if it does not exist and populates it with sample data.
- Used **parameterized queries** and **duplicate email checks** to avoid errors on repeated runs.


## Assumptions and Trade-offs

-> Passwords in the sample data and initial insertions are stored in plain text. In a production app, these should always be hashed before storage.
-> The current design uses SQLite with a single connection per request. For scalability and concurrency, a more robust database or connection pooling might be needed.
-> Authentication and session management are minimal, focusing on core CRUD operations.
-> API security such as rate limiting, input sanitization, and logging were outside this refactor’s scope but would be essential for production.


## What are the other changes could be improved with more time ?

-> Implement full password hashing and secure authentication flows.
-> Add unit and integration tests for all routes and database operations.
-> Use Flask Blueprints to better organize routes by resource.
-> Implement pagination and filtering on user list endpoints.
-> Add comprehensive logging and monitoring.
-> Transition to using an ORM like SQLAlchemy for better database abstraction.


To Run this Project Follow the below steps. 

## How To Run
1. Initialize the database:

   ```bash
   python init_db.py
   ```bash
   python app.py
