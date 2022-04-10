#!/usr/bin/python3
"""module doc"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    if (len(session.query(State).order_by(State.id).all()) < 1):
        print("Nothing")
    else:
        state = session.query(State).order_by(State.id).all()
        print("{}: {}".format(state[0].id, state[0].name,))
