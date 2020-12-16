#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, data):
        super().__init__()
        self.email = data.get("email", "")
        self.password = data.get("password", "")
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
