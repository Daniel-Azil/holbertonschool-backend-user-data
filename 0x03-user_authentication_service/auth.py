#!/usr/bin/env python3
"""
    A module that retrieves password argument and return it's bytes.
"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound

def _generate_uuid() -> str:
    """Generate and return a new UUID as a string"""
    return str(uuid4())


def _hash_password(password: str) -> str:
    """Returns a salted hash of the input password"""
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Return the User object"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            bcrypt_password = _hash_password(password=password)
            return self._db.add_user(email=email,
                                     hashed_password=bcrypt_password)
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the login credentials are valid"""
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode(),
                                  hashed_password=found_user.hashed_password)


    def create_session(self, email: str) -> str:
        """Assigns a new session ID to the user and returns it as a string"""
        try:
            account = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            account.session_id = _generate_uuid()
            return account.session_id


    def get_user_from_session_id(self, session_id: str) -> Union[None, U]:
        """
            Retrieve the user associated with the given session ID, or
            return None if not found.
        """
        if session_id is None:
            return None

        try:
            retrieved_user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return retrieved_user



    def destroy_session(self, user_id: int) -> None:
        """Sets the session ID of the specified user to None."""
        try:
            account = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        account.session_id = None


    def get_reset_password_token(self, email: str) -> str:
        """Generate and return a new reset token for the user."""
        try:
            user_record = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        user_record.reset_token = _generate_uuid()
        return user_record.reset_token


    def update_password(self, reset_token: str, password: str) -> None:
        """Hash the new password and update the user's password field."""
        try:
            user_record = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            user_record.hashed_password = _hash_password(password=password)
            user_record.reset_token = None
