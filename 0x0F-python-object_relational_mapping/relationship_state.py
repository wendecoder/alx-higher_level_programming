#!/usr/bin/python3

"""
    this module contains a Base and State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
        State class inherits the Base class
        Attributes:
            id (int)
            name (string)
            cities (sqlalchemy.orm.relationship)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
