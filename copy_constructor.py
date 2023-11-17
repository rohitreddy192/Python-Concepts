# Copy constructor is not explicitly allowed in Python but can be implemented.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        # Creating a new instance and copying attributes
        return Point(self.x, self.y)

# Creating an instance of the Point class
p1 = Point(3, 4)

# Using the copy method to create a new instance
p2 = p1.copy()

# Displaying attributes of the copied instance
print(f"p2.x: {p2.x}, p2.y: {p2.y}")  # Output: p2.x: 3, p2.y: 4


# There are two types of copies 
# -> Shallow Copy
# -> Shallow copy, copies the objects with its references and don't copy the nested objects properly.

import copy

# Creating a list with nested lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the list
shallow_copied_list = copy.copy(original_list)

# Modifying the shallow copied list
shallow_copied_list[0][0] = 99

print(original_list)         # Output: [[99, 2, 3], [4, 5, 6]]
print(shallow_copied_list)   # Output: [[99, 2, 3], [4, 5, 6]]


# -> Deep Copy
# -> Deep Copy, on the other side copies without the references and into the nested objects properly.

import copy

# Creating a list with nested lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the list
deep_copied_list = copy.deepcopy(original_list)

# Modifying the deep copied list
deep_copied_list[0][0] = 99

print(original_list)         # Output: [[1, 2, 3], [4, 5, 6]]
print(deep_copied_list)      # Output: [[99, 2, 3], [4, 5, 6]]
