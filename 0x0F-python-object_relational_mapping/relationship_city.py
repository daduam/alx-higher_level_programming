#!/usr/bin/python3
"""Relationship City"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey

from relationship_state import Base


class City(Base):
    """Defines City model"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(ForeignKey("states.id"))
