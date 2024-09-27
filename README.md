# FastAPI User Registration System

This project is a simple user registration system built with FastAPI and MySQL. It allows users to register through a web interface and stores their information in a MySQL database.

## Features

- User registration form with client-side validation
- Data storage in MySQL database
- Display of registered users in a table
- FastAPI backend with RESTful API endpoints

## Technologies Used

- FastAPI
- MySQL
- SQLAlchemy
- HTML/CSS/JavaScript

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/fastapi-user-registration.git
   cd fastapi-user-registration
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install fastapi uvicorn sqlalchemy mysqlclient pydantic[email]
   ```

4. Set up your MySQL database:
   - Create a new database named `fastapi_users`
   - Update the `SQLALCHEMY_DATABASE_URL` in `main.py` with your MySQL credentials

## Usage

1. Start the FastAPI server:
   ```
   python main.py
   ```

2. Open a web browser and navigate to `http://localhost:8005`

3. Use the registration form to add new users

4. View the list of registered users in the table below the form


<img width="325" alt="Screenshot 2024-09-27 at 9 18 34 AM" src="https://github.com/user-attachments/assets/857bf54d-da38-4596-9505-73a072f2aba3">


