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

# Base Class


class Vehicle:
    pass

# Subclass Vehicles


class GroundVehicle(Vehicle):
    pass


class FlightVehicle(Vehicle):
    pass

# Subclass Ground Vehicles


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# Subclass Flight Vehicles


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass
