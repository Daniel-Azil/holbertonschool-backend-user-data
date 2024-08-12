"""
    A module that utilises SQLAlchemy to create User model for
    database table named users
"""
from sqlalchemy import Column, integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
        A class that creates the user model
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

    def __repr__(self):
        """
            A function that returns class attributes
        """
        return "<User(name='%s', email='%s', session_id='%s')>" % (
                             self.name, self.email, self.session_id)
