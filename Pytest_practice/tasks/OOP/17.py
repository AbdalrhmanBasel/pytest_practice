# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, rating):
        super().__init__(name, max_speed, mileage)
        self.rating = rating


School_bus = Bus("School Volvo", 100, 12, 4.2)
print(f"A {School_bus.name} has arrived. It's speed {School_bus.max_speed}. Mileage speed was {School_bus.mileage}.I "
      f"would give {School_bus.rating} for this care.")
