#!/usr/bin/env python3
"""Auth Class"""
from db import DB
from user import User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4
from typing import TypeVar, Union

def _hash_password(password: str) -> str:
    """return salted hash of the input password
    hashed with bcrypt.hashpw"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """
    _generate_uuid.
    """
    return str(uuid4())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers and returns a new user if email isn't listed"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        valid_login.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
