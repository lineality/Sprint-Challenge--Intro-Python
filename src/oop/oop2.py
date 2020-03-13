# Test OK
# To the GroundVehicle class, add method drive() that returns "vroooom".
# 
# Instructions: 
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

# creating OOP class
class GroundVehicle():
    # constructor method (function)
    def __init__(self, num_wheels = 4):
        # attribute
        self.num_wheels = num_wheels

    # class method (function), behavior
    def drive(self):
        return "vroooom"

# Subclass Motorcycle from GroundVehicle.
#
# instructions:
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# https://www.geeksforgeeks.org/python-super-in-single-inheritance/

class Motorcycle(GroundVehicle):
    # constructor method (function)
    # give it an additional name attribute
    def __init__(self):
        # manage inheritance with super()
        # inherited attributes
        super().__init__(num_wheels = 2)

    # class methond (function), behavior
    def drive(self):
        return "BRAAAP!!"

# This automatically generates a set of instances of the above OOP classes:
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# instructions:
# Go through the vehicles list and print the result of calling drive() on each.

# iterates through the list of vehicles to test
for i in vehicles: print(i.drive())
