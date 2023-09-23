#!/usr/bin/python3
# File: 100-relationship_states_cities.py
# Author: Oluwatobiloba Light
"""
Creates the State “California” with the City “San Francisco” from the database
hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from relationship_city import City, Base
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
