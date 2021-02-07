#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import Base
from os import getenv
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in database MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiate an Engine"""
        HBNB_ENV = getenv("HBNB_ENV")
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        r = []
        if cls:
            r = self.__session.query(cls).all()
        else:
            for cls in (State, City, Place, Amenity, Review, User):
                r.extend(self.__session.query(cls).all())
        return {"{}.{}".format(type(cls).__name__, cls.id): cls for cls in r}

    def reload(self):
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

    def new(self, obj):
        """ Add a new object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Pending information on db session to be flushed into database """
        self.__session.commit()

    def delete(self, obj=None):
        """  Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """  close the session object """
        self.__session.close()
