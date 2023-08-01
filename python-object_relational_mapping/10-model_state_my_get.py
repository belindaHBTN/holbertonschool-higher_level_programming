#!/usr/bin/python3
"""Display the id of the project that been searched by name"""

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
            State.name == '{}'.format(argv[4])).order_by(State.id)
    for state in states:
        if state is None:
            print("Not found")
        print("{}".format(state.id,))
