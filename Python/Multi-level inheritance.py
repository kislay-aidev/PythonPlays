class Car:
    @staticmethod
    def start():
        print("Car started...")
        
    @staticmethod
    def stop():
        print("Car Stopped.")
        
class ToyotaCar(Car):
     #property from Car
     def __init__ (self, brand):
         self.brand = brand
         
class Fortuner (ToyotaCar):
    #property from ToyotaCar
    def __init__ (self, type):
        self.type = type
        
car1 = Fortuner("Diesel")
car1.start()