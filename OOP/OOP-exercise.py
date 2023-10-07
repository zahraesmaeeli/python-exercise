class Vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def description(self):
        print(f"Brand: {self.model}")
        print(f"Year: {self.year}")


class car(Vehicle):
    def __init__(self,model,year,color,price,tire):
        super().__init__(model,year)
        self.color=color
        self.price=price
        self.tire=tire
    def description(self):
        super().description()
        print("This is car.")

class Motorcycle(Vehicle):
    def __init__(self, model, year, color, price,tire):
        super().__init__(model, year)
        self.color = color
        self.price = price

    def description(self):
        super().description()
        print("This is Motorcycle.")


car=car("prado",2019,"Black",50.5,4)
car.description()

print()