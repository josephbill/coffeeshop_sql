import sqlite3
"""
Coffee class for the Coffee Shop domain model.

Represents a coffee type with:
- Name validation (minimum 3 characters)  
- Relationship to orders
- Methods to analyze order statistics
"""

class Coffee:
    # Class variable to track all coffee instances
    all_coffees = []
    DB_PATH = "coffee_shop.db"  # Database file path

    def __init__(self, name, id=None):
        """
        Initialize a Coffee instance.
        
        Args:
            name (str): Coffee name (minimum 3 characters)
        """
        self.name = name  # Uses the property setter
        self.id = id
        self._orders = []  # List to store associated orders
        Coffee.all_coffees.append(self)  # Add to class tracking list

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
            ValueError: If name is not a string or too short
        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value

    def orders(self):
        """
        Get all orders for this coffee type.
        
        Returns:
            list[Order]: List of Order instances for this coffee
        """
        return self._orders

    def customers(self):
        """
        Get unique list of customers who ordered this coffee.
        
        Returns:
            list[Customer]: Unique Customer instances who ordered this coffee
        """
        return list({order.customer for order in self._orders})

    def num_orders(self):
        """
        Get total number of times this coffee has been ordered.
        
        Returns:
            int: Count of orders for this coffee
        """
        return len(self._orders)

    def average_price(self):
        """
        Calculate average price for this coffee across all orders.
        
        Returns:
            float: Average price or 0 if no orders exist
        """
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
    
    # database methods 
    @classmethod
    def create_table(cls):
        # connection reference : 
        conn = sqlite3.connect(cls.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS coffees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)""")
        conn.commit() #commits the changeaction 
        conn.close() #close the connection 
        
    def save(self):
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        # check if the coffee already exists in the database
        if self.id is None:
            # Kindly know why this is needed
            # first fetch and check if the coffee already exists
            cursor.execute(f"SELECT id FROM coffees WHERE name = ?", (self.name,))  
            existing_coffee = cursor.fetchone() # returns list / single row 
            if existing_coffee:
                # If it exists, set the id to the existing coffee's id
                self.id = existing_coffee[0]
                return
            else:
                # If it doesn't exist, insert a new coffee
                cursor.execute(f"INSERT INTO coffees (name) VALUES (?)", (self.name,))
                self.id = cursor.lastrowid
        else:
            # update 
            cursor.execute(f"UPDATE coffees SET name = ? WHERE id = ?", (self.name, self.id))
        conn.commit()
        conn.close()
            