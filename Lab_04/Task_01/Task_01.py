class Car:
    """
    Class to create car instances.

    Attributes:
      brand: car brand
      model: car model
      year: year of release
      speed: current speed (0 by default)

    Methods:
      accelerate: adds 5 to the current speed
      brake: subtracts 5 from the current speed
      get_speed: returns the current speed
    """

    def __init__(self, brand, model, year):
        """
        Initialize a car instance.

        Args:
          brand: car brand
          model: car model
          year: year of release
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        """Increases speed by 5."""
        self.speed += 5

    def brake(self):
        """Decreases speed by 5."""
        self.speed -= 5

    def get_speed(self):
        """Returns the current speed."""
        return self.speed

    def display_info(self):
        """Displays the car's brand, model, year, and current speed."""
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Speed: {self.speed} km/h"

car = Car("Audi", "RS6", 2022)
print(car.display_info())

for _ in range(5):
    car.accelerate()
    print(car.display_info())

for _ in range(5):
    car.brake()
    print(car.display_info())
