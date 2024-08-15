# User Authentication Service

This project implements a user authentication service using Flask, SQLAlchemy, and bcrypt. It is designed to teach the basics of authentication systems by building them from scratch.

## Setup

```bash
pip3 install bcrypt

## User Model

Defines a `User` model with the following attributes:

- `id`: Primary key
- `email`: Non-nullable string
- `hashed_password`: Non-nullable string
- `session_id`: Nullable string
- `reset_token`: Nullable string


## DB Class

The `DB` class manages the database:

- `add_user(email, hashed_password)`: Adds a user to the database.
- `find_user_by(**kwargs)`: Finds a user by arbitrary attributes.
- `update_user(user_id, **kwargs)`: Updates user attributes.


## Password Hashing

```python
from auth import _hash_password

print(_hash_password("YourPassword"))


## Register User

Register a new user:

```python
from auth import Auth

auth = Auth()
auth.register_user("email@example.com", "password")



## Basic Flask App

Run the Flask app:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")


## Register User Endpoint

Register a user via the `/users` endpoint:

```bash
curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd'
