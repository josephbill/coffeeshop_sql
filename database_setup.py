from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

def setup_database():
    Customer.create_table()
    Coffee.create_table()
    # Order.create_table()
    
if __name__ == "__main__":
    print("=== Setting up database tables ===")
    setup_database()
    print("=== Database setup completed ===")