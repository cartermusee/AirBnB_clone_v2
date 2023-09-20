#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade="all, delete")
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False, backref='place')
    else:
        @property
        def reviews(self):
            """reviews getter"""
            from model import Storage
            from models.review import Review
            reviews_do = []

            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_do.append(review)
            return reviews_do

        @property
        def amenities(self):
            """amenities  getter"""
            from model import Storage
            from models.amenity import Amenity
            amenity_do = []

            for amenity in storage.all(Amenity).values():
                if amenities.amenity_id == self.id:
                    reviews_do.append(amenities)
            return reviews_do

        @amenities.setter
        def amenities(self, obj=None):
            """setter"""
            from models.amenity import Amenity
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
