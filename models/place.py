#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        if data:
            self.city_id = data.get("city_id", "")
            self.user_id = data.get("user_id", "")
            self.name = data.get("name", "")
            self.description = data.get("description", "")
            self.number_rooms = data.get("number_rooms", 0)
            self.number_bathrooms = data.get("number_bathrooms", 0)
            self.max_guest = data.get("max_guest", 0)
            self.price_by_night = data.get("price_by_night", 0)
            self.latitude = data.get("latitude", 0.0)
            self.longitude = data.get("longitude", 0.0)
            self.amenity_ids.append(data.get("amenity_ids", ""))
