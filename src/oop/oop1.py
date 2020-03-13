# Test OK
# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

### GGA Answers

# main parent class (base class)
# create OOP class
# Vehicle
class Vehicle:
    pass

# child-class 1 of (base class) Vehicle class
# FlightVehicle
class FlightVehicle(Vehicle):
    pass

# child-class 1 of (base class) FlightVehicle class
# Starship
class Starship(FlightVehicle):
    pass

# child-class2 of (base class) FlightVehicle class
# Airplane
class Airplane(FlightVehicle):
    pass

# child-class 2 of (base class) Vehicle class
# GroundVehicle
class GroundVehicle(Vehicle):
    pass

# child-class 1 of (base class) GroundVehicle
# Car
class Car(GroundVehicle):
    pass

# child-class 2 of (base class) GroundVehicle
# Motorcycle
class Motorcycle(GroundVehicle):
    pass