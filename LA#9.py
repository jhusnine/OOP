class Car:
    def __init__(self, brand):
        cars_brand = brand

    def __str__(self):
        return f"{self.brand}"

cars = Car("Ford")
print(cars)
del cars
print(cars)