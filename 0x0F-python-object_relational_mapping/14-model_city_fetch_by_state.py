#!/usr/bin/python3
'''
a script 14-model_city_fetch_by_state.py that prints all
 City objects from the database hbtn_0e_14_usa
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
