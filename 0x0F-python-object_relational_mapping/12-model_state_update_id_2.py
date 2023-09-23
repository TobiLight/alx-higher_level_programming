#!/usr/bin/python3
# File: 10-model_state_my_get.py
# Author: Oluwatobiloba Light
"""
Prints the State object with the name passed as argument from the database
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
    session = Session()
    q = session.query(State).filter(State.id == 2).first()
    if q:
        q.name = "New Mexico"
        session.commit()
