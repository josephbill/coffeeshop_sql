from models.base import Base , engine
def setup_database():
    # create all tables in db via the engine 
    Base.metadata.create_all(engine)
    # Customer.create_table()
    # Coffee.create_table()
    # Order.create_table()
    
if __name__ == "__main__":
    print("=== Setting up database tables ===")
    setup_database()
    print("=== Database setup completed ===")