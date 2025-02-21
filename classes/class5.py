"""Create a class Vehicle with attributes brand and year.

Add a method show_info().
Create a subclass Car that adds a model attribute and 
overrides show_info()."""

# Class vehicle
class Vehicle:
    # self method
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def show_info(self):
        print(f"brand {self.brand}, year {self.year}")
    

# class car
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model


    def show_info(self):
        print(f"brand {self.brand}, year {self.year}, model {self.model}")
        

v = Vehicle("Toyota", 2020)
v.show_info()

c = Car("Toyota", 2020, "Corolla")
c.show_info()