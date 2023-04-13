#!/usr/bin/python3
"""Model State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines State model"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
