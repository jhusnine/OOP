'''WEEK#


THE PASS STATEMENT 

PASS 
  - place holder
  
  
class student:
    pass
jhusnine = student()
print("jhusnine")

\
class laptop():
    
    def __init__(self, brand, model):
        pass
    def laptop_info(self):
        pass           
Laptop = laptop("Asus", "VivoBook Series")
print(Laptop.laptop_info())'''
#MODIFY 
class course:
    def __init__(self, name):
        self.name = name

IT = course("Information Technology")
CS = course("Computer Science")
print(CS.name)
CS.name = "Bsit"
print(CS.name)


#LA#7
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

# DELETE OBJECT PROPERTIES
# you can del keyword object 
class food:
    def __init__(self, name):
        self.name = name
burger = food("Angels")
del burger.name
print(burger.name)

#DELETE OBJECT
class food:
    def __init__(self, name):
        self.name = name
burger = food("Angels")
del burger
print(burger.name)
