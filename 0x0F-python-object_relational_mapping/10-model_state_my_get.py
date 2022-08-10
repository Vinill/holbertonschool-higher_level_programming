#!/usr/bin/python3
""" script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa """

import MySQLdb
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if __name__ == "__main__":

    arg4 = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], arg4), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    class State(Base):
        """Instatiation of class"""

        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, unique=True,
                    autoincrement=True, nullable=False)

        name = Column(String(128), nullable=False)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = session.query(State).filter(State.name.like(arg4))

        if (result.all()):
            for state in result:
                print(state.id)
        else:
            print("Not found")
