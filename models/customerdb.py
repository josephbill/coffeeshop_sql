from sqlalchemy import Column, Integer , String , DateTime
from sqlalchemy.orm import relationship
from .base import Base 
class Customer(Base):
    # optional define the tablename
    __tablename__ = "customers"
    
    # define the columns // this columns should map from an initialization persepective 
    # but to keep object creation separate from this declaration 
    # define the columns as class variables
    # sqlalchemy data types 
    # sqlalchemy constraint attributes i.e. primary_key , nullable , unique , default
    id = Column(Integer, primary_key = True)
    name = Column(String(15), nullable= False)
    created_at = Column(DateTime, default=DateTime.now)
    
    # customer has a relationship with orders , one customer can have many orders
    # the reference variable is the name of the class to relate with in a plural format 
    # back_populates is used to create a bidirectional relationship
    # orders.customer : because of backpopulate this attr returns orders for a customer 
    # customer.orders : because of backpopulate this attr returns customer for an order
    # the reference variable is the name of the class to relate with in a singular format
    # in this domain I want to delete all orders for a customer when the customer is deleted
    # cascade attribute is used to specify the behavior when the parent object is deleted
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")
    # orders = relationship("Order", back_populates="customer", cascade="save-update, merge")
    
    def __init__(self, name):
        self.name = name
        # self.orders = []  # Initialize an empty list for orders
        # self.coffees = []  # Initialize an empty list for coffees
        
    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}')"
    
    def coffees(self):
        return list({order.coffee for order in self.orders})
