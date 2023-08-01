#!/usr/bin/python3
"""List all State objects that contain the letter a from db"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Start link class to table in database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Querying"""
    states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
