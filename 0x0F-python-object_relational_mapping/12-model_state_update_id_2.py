#!/usr/bin/python3
'''
Script that changes the name of a State object from
 the database hbtn_0e_6_usa
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
    searched = session.query(State).filter(State.id == '2')
    searched.name = 'New Mexico'
    session.commit()
