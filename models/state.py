#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        if data:
            self.name = data.get("name", "")
