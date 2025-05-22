import sqlite3
"""
Customer class for the Coffee Shop domain model.

Represents a coffee shop customer with:
- Name validation (1-15 characters)
- Relationship to orders
- Methods to manage coffee orders
"""



class Customer:
    # Class variable to track all customer instances
    all_customers = []
    DB_PATH = "coffee_shop.db"  # Database file path

    def __init__(self, name):
        """
        Initialize a Customer instance.
        
        Args:
            name (str): Customer name (1-15 characters)
        """
        self.name = name  # Uses the property setter
        self._orders = []  # List to store associated orders
        Customer.all_customers.append(self)  # Add to class tracking list

    @property
    def name(self):
        """Getter for name property."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter for name property with validation.
        
        Args:
            value (str): New name value
            
        Raises:
            ValueError: If name is not a string or length is invalid
        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        """
        Get all orders placed by this customer.
        
        Returns:
            list[Order]: List of Order instances for this customer
        """
        return self._orders

    def coffees(self):
        """
        Get unique list of coffees ordered by this customer.
        
        Returns:
            list[Coffee]: Unique Coffee instances ordered by this customer
        """
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from models import Order
        """
        Create and associate a new order for this customer.
        
        Args:
            coffee (Coffee): Coffee being ordered
            price (float): Order price (1.0-10.0)
            
        Returns:
            Order: The newly created order
            
        Note:
            Automatically adds the order to the customer's order list
        """
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        from models import Coffee
        """
        Find the customer who spent the most on a specific coffee.
        
        Args:
            coffee (Coffee): Coffee to evaluate
            
        Returns:
            Customer or None: Top spending customer or None if no orders exist
            
        Note:
            Evaluates all customers who ordered the specified coffee
        """
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide a Coffee instance")
        
        max_spent = 0
        top_customer = None
        
        for customer in cls.all_customers:
            # Calculate total spent by this customer on the specified coffee
            # dictionary accumulation {"customer" : "total spent"} , look dictionary to get spent value  
            customer_spent = sum(
                order.price 
                for order in customer.orders() 
                if order.coffee == coffee
            )
            
            if customer_spent > max_spent:
                max_spent = customer_spent
                top_customer = customer
                
        return top_customer
    
        # database methods 
    @classmethod
    def create_table(cls):
        # connection reference : 
        conn = sqlite3.connect(cls.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT FALSE)""")
        conn.commit() #commits the changeaction 
        conn.close() #close the connection 