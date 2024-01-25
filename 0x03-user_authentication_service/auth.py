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
