#OOPS Getter, Setter methods with protected access..
class Car:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

# Creating an object of the Car class
car = Car("Toyota", "Corolla")

# Accessing getter methods
print(car.brand)  # Output: Toyota
print(car.model)  # Output: Corolla

# Using setter methods
car.brand = "Tesla"
car.model = "Model S"

# Accessing attributes after modification
print(car.brand)  # Output: Tesla
print(car.model)  # Output: Model S


