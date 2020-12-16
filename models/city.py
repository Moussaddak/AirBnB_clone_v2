#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        if data:
            self.name = data.get("name", "")
            self.state_id = data.get("state_id", "")
