class Car:
    country = "Turkey"

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def speed(self):
        print("Beast in Speed")


class Audi(Car):
    def speed(self):

        super().speed()

        return "250 km/h"


a = Audi("The successor", "KO21", 2022)
a.speed()
print(a.country)