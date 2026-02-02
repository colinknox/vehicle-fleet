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

class Truck(Vehicle):
    def __init__(self, make, model, year, bed_length):
        super().__init__(make, model, year)
        self.bed_length = bed_length

    def get_bed_info(self):
        return f"Bed length: {self.bed_length} feet"



f150 = Truck("Ford", "F150", 2025, 6)

print(f150.make)
print(f150.model)
print(f150.year)
print(f150.bed_length)
print(f150.get_bed_info())