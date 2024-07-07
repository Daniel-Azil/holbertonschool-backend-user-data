# Holberton School Backend User Data

This repository contains a collection of backend projects related to user authentication and session management. These projects are part of the Holberton School curriculum designed to help students understand the key concepts and implementations of various authentication mechanisms used in modern web applications.

## Projects

### 0x01 - Basic Authentication
This project demonstrates the implementation of basic authentication for a web application. Basic authentication is a simple method for enforcing access control to web resources where a username and password are sent in the HTTP header.

#### Features:
- User authentication using HTTP Basic Authentication.
- A simple authentication scheme to check the username and password.

### 0x02 - Session Authentication
This project focuses on session-based authentication. Sessions are used to store user data between requests on the server-side, which allows a user to remain logged in as they interact with the application.

#### Features:
- User login and logout with session management.
- Securely store and retrieve session data.
- Protect routes requiring user authentication.

### 0x03 - User Authentication Service
This project integrates user authentication in a complete service. It demonstrates the combination of various authentication techniques, such as basic authentication and session management, to create a comprehensive authentication system.

#### Features:
- Registration and login system with encrypted passwords.
- Use of secure cookie storage for session handling.
- Password validation and error handling.

## Technologies Used
- Python
- Flask
- SQLAlchemy
- HTTP/HTTPS
- Cookie and session management

## Requirements
- Python 3.8 or higher
- Flask
- SQLAlchemy
- Flask-Login
- Flask-WTF

## Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/holbertonschool-backend-user-data.git
   cd holbertonschool-backend-user-data
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3.  **Install the required packages:**

    ```bash
    Copy code
    pip install -r requirements.txt
    ```

## Usage

Run the Flask development server:

```bash
flask run
```
Access the application at http://127.0.0.1:5000/ in your browser.

Test the authentication mechanisms by accessing the routes that require authentication.





