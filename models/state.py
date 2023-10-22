#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv("HBNB_MYSQL_DB") != "db":
        @property
        def cities(self):
            """getter"""
            from models.city import City
            from models import storage

            lts = []
            city_lts = storage.all(City)
            for city in city_lts.values():
                if city.state_id == self.id:
                    lts.append(city)
            return lts
