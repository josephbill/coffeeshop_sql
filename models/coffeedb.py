from sqlalchemy import Column, Integer , String 
from sqlalchemy.orm import relationship
from .base import Base 
class Coffee(Base):
    __tablename__ = "coffees"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(15), nullable= False)
    orders = relationship("Order", back_populates="coffee", cascade="all, delete-orphan")
    
    def __init__(self, name):
        self.name = name
      