#!/usr/bin/python3
"""Relationship State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines State model"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", cascade="all", backref="state")
