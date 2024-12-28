#!/usr/bin/python3
"""
python file that contains the class definition of a class
City that enhirits from the class Base
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''
    class City that enhirits from Base
    Attributes:
    id (int): id of the state
    name (str): name of the state
'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
