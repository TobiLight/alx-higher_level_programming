#!/usr/bin/python3
# File: 9-model_state_filter_a.py
# Author: Oluwatobiloba Light
"""
Lists all State objects that contain the letter a from the database
hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)
    Session = scoped_session(session_factory)
    q = Session()
    q = q.query(State).order_by(State.id).filter(State.name.like('%a%'))
    for item in q:
        print("{}: {}".format(item.id, item.name))
