from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # cursor object 
from sqlalchemy import create_engine # connection object

DATABASE_URL = "sqlite:///coffee_sqlalchemy.db"  # load live database / hosted db 
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine) # session blueprint 
Base = declarative_base() # Base class for all models 