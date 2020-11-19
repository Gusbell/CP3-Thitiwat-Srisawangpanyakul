class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    def model(self):
        print("This's Pickup")

class Car(Vehicle):
    def model(self):
        print("This's Car")

class Van(Vehicle):
    def model(self):
        print("This's Van")

class Estatecar(Vehicle):
    def model(self):
        print("This's Estatecar")

pickup1 = Pickup()
pickup1.model()
pickup1.turnOnAirConditioner()
car1 = Car()
car1.model()
car1.turnOnAirConditioner()
van1 = Van()
van1.model()
van1.turnOnAirConditioner()
estatecar1 = Estatecar()
estatecar1.model()
estatecar1.turnOnAirConditioner()

