#!/usr/bin/python3
"""Model City"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey

from model_state import Base


class City(Base):
    """Defines City model"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(ForeignKey("states.id"))
