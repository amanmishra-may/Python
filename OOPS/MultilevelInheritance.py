#MultilevelInheritance : class1 inherit base class and class2 inherit(1 class) & class3 inherit (class2)

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

class Fortuner(Toyotacar) :
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
