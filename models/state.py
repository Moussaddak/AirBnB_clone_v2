#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """

    """ Definition of cities table structure"""
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        if data:
            self.name = data.get("name", "")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        from models import storage

        @property
        def cities(self):
            return [state for state in self.storage.all(City).value()
                    if state.state_id == self.id]
