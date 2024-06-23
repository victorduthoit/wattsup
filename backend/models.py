from sqlalchemy import Column, Integer, String, Float, JSON
from database import Base

class Appliance(Base):
    __tablename__ = "appliances"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    category = Column(String, index=True)
    power = Column(Float)
    duration = Column(Float, nullable=True)
    consumption = Column(Float, nullable=True)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    possible_duration = Column(JSON)
    minimum_duration = Column(Float)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, index=True)
    email = Column(String)