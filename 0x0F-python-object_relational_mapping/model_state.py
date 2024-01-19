#!/usr/bin/python3
"""Write a python file that contains the class definition
of a State and an instance Base = declarative_base():"""

from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
