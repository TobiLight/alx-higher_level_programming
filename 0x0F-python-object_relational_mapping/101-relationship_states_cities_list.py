#!/usr/bin/python3
# File: 101-relationship_states_cities_list.py
# Author: Oluwatobiloba Light
"""
Lists all State objects, and corresponding City objects, contained in the
database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(State).order_by(State.id)
    
    for state in q:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
