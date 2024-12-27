#!/usr/bin/python3
"""
python file that contains the class definition of a State and an instance Base
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    '''
    class state that enhirits from Base
    attributes:
    id (int): id of the state
    name (str): name of the state
'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
