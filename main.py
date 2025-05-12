# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand          # Encapsulated attribute
        self._model = model
        self._year = year

    def display_info(self):
        print(f"{self._year} {self._brand} {self._model}")

    def move(self):
        print("This vehicle moves in its own way.")

# Subclasses with overridden methods (Polymorphism)
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

# Example usage
if __name__ == "__main__":
    car = Car("Tesla", "Model S", 2022)
    plane = Plane("Boeing", "747", 2015)
    boat = Boat("Yamaha", "WaveRunner", 2020)

    vehicles = [car, plane, boat]

    for v in vehicles:
        v.display_info()
        v.move()
        print("-" * 30)
