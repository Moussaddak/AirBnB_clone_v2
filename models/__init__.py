#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")
if HBNB_TYPE_STORAGE == "db":
    """ Using MySQL database for storage """
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    """ Using Json file for storage """
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
