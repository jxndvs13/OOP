class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, seats, speed):
        Vehicle.__init__(self, make, model, year)
        self.seats = seats
        self.speed = speed
    def display(self):
        print("")
        Vehicle.display(self)
        print(f"# of Seats: {self.seats}\n"
              f"Max Speed: {self.speed}")

class Truck(Vehicle):
    def __init__(self, make, model, year, tires,load):
        Vehicle.__init__(self, make, model, year)
        self.tires = tires
        self.load = load
    def display(self):
        print("")
        Vehicle.display(self)
        print(f"# of Tires: {self.tires}\n"
              f"Max Load: {self.load}")

C1 = Car("Kia","Optima","2008","5","120 mph")
C1.display()
T1 = Truck("Ford","F150, Oklahoma Edition","2006","4","1000 lb")
T1.display()