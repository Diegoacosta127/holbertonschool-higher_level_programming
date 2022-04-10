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
    a = 0
    for state in session.query(State).order_by(State.id).all():
        if argv[4] == state.name:
            print("{}".format(state.id))
            a = 1
    if a == 0:
        print('Not found')
