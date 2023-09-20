#!/usr/bin/python3
"""module for db storage"""
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """endine class"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getenv("HBNB_MYSQL_USER"),
                                             os.getenv("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(Bind=self.__engine)

    def all(self, cls=None):
        """create a session"""
        from models import base_model
        object_dict = {}
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                objects = self.__session.query(cls).all()
                for ob in objects:
                    key = "{}.{}".format(type(ob).__name__, ob.id)
                    object_dict[key] = ob
        else:
            if type(cls) == str:
                cls = eval(cls)
            class_obj = self.__session.query(cls).all()
            for obj in class_obj:
                object_dict['{}.{}'.format(type(obj).__name__, obj.id)] = obj
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
