#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City."""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """City model to link to the mysql cities"""
    __tablename__ = "cities"

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
