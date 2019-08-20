#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
import models
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City',
                              backref='state', 
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """getter cities attributes in file storage
            """
            return [city for city in models.storage.all(City)
                    if city.state_id == self.id]
