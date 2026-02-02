class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
    
    def age(self):
        return 2026 - self.year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_door_info(self):
        return f"This car has {self.num_doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def get_sidecar_info(self):
        return f"Has sidecar: {self.has_sidecar}"



brough = Motorcycle("Brough", "Superior", 1932, False)

print(brough.get_sidecar_info())