#!/usr/bin/env python3
"""
    A module that complete the DB class provided below
    to implement the add_user method.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            A method that adds a new user to the database
            Args:
                email (str): Email address of the user
                hashed_password (str): User's password hashed with byscript
            Return:
                User: A new user object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
            A method that finds a user by a given attribute
        """
        if kwargs is None:
            raise InvalidRequestError
        for each_key in kwargs.keys():
            if each_key not in User.__table__.columns.keys():
                raise InvalidRequestError
        result = self._session.query(User).filter_by(**kwargs).first()
        if result is None:
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            A method that updates a user by a given attribute
            Args:
                user_id (int): The ID of the user to update.
                **kwargs: Keyword arguments representing the
                          attributes to update.
        """
        current_user = self.find_user_by(id=user_id)
        for attribute in kwargs.keys():
            if attribute not in User.__table__.columns.keys():
                raise ValueError
        for attribute, value in kwargs.items():
            setattr(current_user, attribute, value)
        self._session.commit()
