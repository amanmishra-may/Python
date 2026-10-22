#Inheritance -> when one class derives the properties and methods of another class.


class Car :
    color = "black"
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")

class Toyotacar(Car) :
    def __init__(self,name):
        self.name = name

car1 = Toyotacar("Fortuner")
car2 = Toyotacar("Prius")

print(car1.start())
print(car1.color)