#!/usr/bin/python3
# File: 14-model_city_fetch_by_state.py
# Author: Oluwatobiloba Light
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'
                           .format(sys.argv[1], sys.argv[2], 3306,
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)
    Session = scoped_session(session_factory)
    q = Session()
    q = q.query(City, State).order_by(City.id).filter(
        City.state_id == State.id).all()
    for state, city in q:
        print("{}: ({}) {}".format(city.name, state.id, state.name))
