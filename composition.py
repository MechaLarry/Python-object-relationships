#with intermediary class
class Parent:

    all = []  # A list to keep track of all Parent objects.

    def __init__(self, name, children=None):
        self.name = name  # Each Parent has a name.
        self._children = []  # Each Parent has a list of children.
        if children:
            for child in children:
                self.add_child(child)  # Add each child to the parent's list.
        Parent.all.append(self)  # Add the parent to the list of all parents.

    def children(self):
        return self._children  # Return the list of the parent's children.

    def add_child(self, child):
        if isinstance(child, Child):
            self._children.append(child)  # Add a Child object to the parent's list.
        else:
            raise ValueError("Child must be an instance of the Child class.")

class Child:

    def __init__(self, name):
        self.name = name  # Each Child has a name.

    def parents(self):
        return [parent for parent in Parent.all if self in parent.children()]
        # Return a list of parents who have this child.

    def add_parent(self, parent):
        if isinstance(parent, Parent):
            parent.add_child(self)  # Add this child to the parent's list.
        else:
            raise ValueError("Parent must be an instance of the Parent class.")

# Example of using the classes
# Create Parent objects
parent1 = Parent('Nick')
parent2 = Parent('Megan')

# Create Child objects
child1 = Child('Steve')
child2 = Child('Liz')

# Establish relationships
parent1.add_child(child1)
parent2.add_child(child1)
child2.add_parent(parent1)
child2.add_parent(parent2)

# Display relationships
print(f"Children of {parent1.name}: {[child.name for child in parent1.children()]}")
print(f"Parents of {child1.name}: {[parent.name for parent in child1.parents()]}")


#with intermediary class
