#!/usr/bin/python3
"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from relationship_city import City, Base
    from relationship_state import State
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
    
    newstate = State(name="California")
    newcity = City(name="San Francisco")

    newstate.cities.append(newcity)

    session.add(newstate)
    session.add(newcity)

    session.commit()
    session.close()