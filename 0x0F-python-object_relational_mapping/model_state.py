#!/usr/bin/python3
""" python file that contains the class definition of a
    State and an instance Base = declarative_base() """

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)

Base = declarative_base()


class State(Base):
    """Instatiation of class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
