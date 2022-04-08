#!/usr/bin/python3
"""module doc"""
from sqlalchemy import Column, Integer, String, create_engine, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                       argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
dele = delete(State).where(State.name.like('%a%'))
engine.execute(dele)
