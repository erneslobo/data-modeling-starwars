import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
import enum

Base = declarative_base()

class Gender(enum.Enum):
    male = 1
    female = 2

class Type_Fav(enum.Enum):
    character = 1
    planet = 2
    vehicle = 3

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(Enum(Gender))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))
    homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet", backref="planet")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    population = Column(Integer)
    url = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Type_Fav))

    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')