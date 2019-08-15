#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from os import getenv
import models
from sqlalchemy.orm import relationship, backref
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade='all, delete-orphan',
                          backref=backref('state', cascade='all, delete-orphan'),
                          passive_deletes=True,
                          single_parent=True)

    @property
    def cities(self):
        """getter cities attributes in file storage
        """
        return {key: value for key, value in models.storage.all().items()
                    if value.state_id == self.id}
