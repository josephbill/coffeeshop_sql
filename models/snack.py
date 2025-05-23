from sqlalchemy import Column , Integer, String 
from models.base import Base 

class Snack(Base):
    __tablename__ = "snacks"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(15), nullable= False)
    calories = Column(Integer)
    
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories