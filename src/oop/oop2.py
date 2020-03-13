# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

# creating OOP class
class GroundVehicle():
    # constructor method (function)
    def __init__(self, num_wheels):
        # attribute
        self.num_wheels = num_wheels

    # class methond (function), behavior
    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# https://stackoverflow.com/questions/2399307/how-to-invoke-the-super-constructor-in-python#2399332

class Motorcycle(GroundVehicle):
    # constructor method (function)
    # give it an additional name attribute
    def __init__(self):
        # note: only self. what is not inherited
        # manage inheritance with super()
        # inherited attributes
        super(GroundVehicle, self, num_wheels = 2).__init__()

    # class methond (function), behavior
    def drive(self):
        return "BRAAAP!!"

# vehicles = [
#     GroundVehicle(),
#     GroundVehicle(),
#     Motorcycle(),
#     GroundVehicle(),
#     Motorcycle(),
# ]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
#for i in vehicles:
  
#Motorcycle.drive(self)
#motorcycle = (Motorcycle, 2)