class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Ford", "Black")
car2 = Car("Honda", "Gray")
print(car1.brand, car1.color)
print(car2.brand, car2.color)

car1.color= "Peach"

print(car1.brand, car1.color)
print(car2.brand, car2.color)
