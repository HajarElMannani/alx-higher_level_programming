#!/usr/bin/python3
'''
Script that prints the first State object from the database hbtn_0e_6_usa
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_inst = session.query(State).order_by(State.id).first()
    if State is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_inst.id, first_inst.name))
