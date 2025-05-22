"""
Order class for the Coffee Shop domain model.

Represents a customer's coffee order with:
- Relationships to Customer and Coffee
- Price validation (1.0-10.0)
"""



class Order:
    # Class variable to track all order instances
    all_orders = []

    def __init__(self, customer, coffee, price):
        """
        Initialize an Order instance.
        
        Args:
            customer (Customer): Customer who placed the order
            coffee (Coffee): Coffee being ordered
            price (float): Order price (1.0-10.0)
        """
        self.customer = customer  # Uses the property setter
        self.coffee = coffee      # Uses the property setter
        self.price = price        # Uses the property setter
        
        # Add to customer's and coffee's order lists
        customer.orders().append(self)
        coffee.orders().append(self)
        
        # Add to class tracking list
        Order.all_orders.append(self)

    @property
    def customer(self):
        """Getter for customer property."""
        return self._customer

    @customer.setter
    def customer(self, value):
        from models import Customer
        """
        Setter for customer property with validation.
        
        Args:
            value (Customer): Customer instance
            
        Raises:
            ValueError: If value is not a Customer instance
        """
        if not isinstance(value, Customer):
            raise ValueError("Must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        """Getter for coffee property."""
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from models import Coffee
        """
        Setter for coffee property with validation.
        
        Args:
            value (Coffee): Coffee instance
            
        Raises:
            ValueError: If value is not a Coffee instance
        """
        if not isinstance(value, Coffee):
            raise ValueError("Must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        """Getter for price property."""
        return self._price

    @price.setter
    def price(self, value):
        """
        Setter for price property with validation.
        
        Args:
            value (float): Order price (1.0-10.0)
            
        Raises:
            ValueError: If price is invalid
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value