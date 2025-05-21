"""
Debug script for testing the Coffee Shop domain model.

Demonstrates:
- Object creation
- Relationship management
- Method functionality
"""

from models.customer import Customer
from models.coffee import Coffee
from models.order import Order
from database_setup import setup_database

def debug():
    # set up database tables
    setup_database() 
    """
    Main debug function to demonstrate model functionality.
    """
    print("=== Creating Customers ===")
    alice = Customer("Alice")
    bob = Customer("Bob")
    print(f"Created customers: {alice.name}, {bob.name}\n")
    
    print("=== Creating Coffees ===")
    latte = Coffee("Latte")
    latte.save()
    espresso = Coffee("Espresso")
    espresso.save()
    cappuccino = Coffee("Cappuccino")
    cappuccino.save()
    print(f"Created coffees: {latte.name}, {espresso.name}, {cappuccino.name}\n")
    
    # print("=== Creating Orders ===")
    # order1 = Order(alice, latte, 4.5)
    # order2 = Order(alice, espresso, 3.0)
    # order3 = Order(bob, latte, 5.0)
    # order4 = Order(bob, cappuccino, 4.0)
    # print(f"Created 4 orders linking customers to coffees\n")
    
    # print("=== Testing Relationships ===")
    # print(f"{alice.name}'s orders:")
    # for order in alice.orders():
    #     print(f"- {order.coffee.name} at ${order.price}")
    
    # print(f"\n{bob.name}'s coffees:")
    # for coffee in bob.coffees():
    #     print(f"- {coffee.name}")
    
    # print(f"\n{latte.name} customers:")
    # for customer in latte.customers():
    #     print(f"- {customer.name}")
    
    # print("\n=== Testing Aggregate Methods ===")
    # print(f"Number of {latte.name} orders: {latte.num_orders()}")
    # print(f"Average price for {latte.name}: ${latte.average_price():.2f}")
    
    # print("\n=== Testing Class Method ===")
    # top_latte_customer = Customer.most_aficionado(latte)
    # print(f"Top {latte.name} customer: {top_latte_customer.name if top_latte_customer else 'None'}")

if __name__ == "__main__":
    print("=== Starting Coffee Shop Model Debug ===")
    debug()
    print("\n=== Debug Completed ===")