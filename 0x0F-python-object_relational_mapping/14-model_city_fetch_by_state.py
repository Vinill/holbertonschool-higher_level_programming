#!/usr/bin/python3
"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    import sys
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session

    user = sys.argv[1]
    passwrd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(user, passwrd, dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
