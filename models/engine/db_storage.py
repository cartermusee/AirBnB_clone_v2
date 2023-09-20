#!/usr/bin/python3
"""module for db storage"""
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.city import Amenity
from models.place import Place
from models.review import Review


class DbStorage():
    """endine class"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getnev("HBNB_MYSQL_USER"),
                                             os.getnev("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getnev("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getnev("HBNB_ENV") == 'test':
            Base.metadata.drop_all(Bind=self.__engine)

    def all(self, cls=None):
        """create a session"""
        from models import base_model
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            objects = []
            for cls in classes:
                objects += self.__sesson.query(cls).all()
        else:
            results = self_session.query(cls).all()

        object_dict = {}

        for obj in results:
            object_dict['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj
        return object_dict

    def new(self, obj):
        """add to db session"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(my_session)
