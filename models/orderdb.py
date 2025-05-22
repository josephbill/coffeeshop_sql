from sqlalchemy import Column, Integer , Float, ForeignKey 
from sqlalchemy.orm import relationship
from .base import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey('customers.id') ,nullable=False)
    coffee_id = Column(Integer, ForeignKey('coffees.id') ,nullable=False)
    price = Column(Float, nullable=False)
    
    # define the relationship with the customer and coffee tables
    customer = relationship("Customer", back_populates="orders")
    coffee = relationship("Coffee", back_populates="orders")
    
    def __init__(self, customer, coffee , price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
    
    