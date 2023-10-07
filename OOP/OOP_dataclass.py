from dataclasses import dataclass
@dataclass
class Employee:
    name:str
    lastname:str
    age:int
    ID:int
    salary:float
Ali=Employee("Ali","ahmadi",26,251689,50.5)
print(Ali.lastname)