#!/usr/bin/python3
"""module doc"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(city.State.name, city.City.id,
              city.City.name))
