class Car:
    def __init__(self, engine):
        self.engine = engine  # A Car has an Engine, but the Engine exists independently.

class Engine:
    def __init__(self, cylinders, fuelType):
        self.cylinders = cylinders  # The Engine has a number of cylinders.
        self.fuelType = fuelType  # The Engine uses a specific type of fuel.

# Example of using the classes
# Create an Engine object
engine = Engine(4, "Gasoline")

# Create a Car object with the Engine object
car = Car(engine)

# Access the attributes of the Car and Engine objects
print(f"The car has an engine with {car.engine.cylinders} cylinders that uses {car.engine.fuelType}.")
