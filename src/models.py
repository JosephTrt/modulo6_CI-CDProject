from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String)
    age = Column(Integer)
    annual_income = Column(Float)
    prediction = Column(String)
