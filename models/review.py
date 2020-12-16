#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, data):
        super().__init__()
        self.place_id = data.get("place_id", "")
        self.user_id = data.get("user_id", "")
        self.text = data.get("text", "")
