class GroceryItem:
    def __init__(self, name, price):
        self.name = name  # Each GroceryItem has a name.
        self.price = price  # Each GroceryItem has a price.

class Shopper:
    def __init__(self, name):
        self.name = name  # Each Shopper has a name.
        self.grocery_items = []  # The Shopper can have many grocery items.

# The following code will execute when the script is run
if __name__ == "__main__":
    # Create GroceryItem objects
    apple = GroceryItem("Apple", 0.5)
    bread = GroceryItem("Bread", 2.0)

    # Create a Shopper object
    shopper = Shopper("Alice")

    # Add items to the shopper's grocery list
    shopper.grocery_items.append(apple)
    shopper.grocery_items.append(bread)

    # Print out the shopper's information
    print(f"Shopper: {shopper.name}")
    print("Grocery Items:")
    for item in shopper.grocery_items:
        print(f"- {item.name}: ${item.price}")