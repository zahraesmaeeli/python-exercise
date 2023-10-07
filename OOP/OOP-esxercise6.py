class Employee:
    def __init__(self, name,role ,salary ):
        self.name = name
        self.role = role
        self.salary = salary

        def get_name(self):
            return self.name

        # def get_role(self):
        #     return self.role

        def get_bonus(self):
            return 0

class Manager(Employee):
    def __init__(self, name,role ,salary):
        super().__init__(name,role ,salary)
    def get_name(self):
        return self.name
    def get_bonus(self):
        return self.salary * 0.19



class Developer(Employee):
    def __init__(self, name, role, salary):
        super().__init__(name, role, salary)

    def get_name(self):
            return self.name
    def get_bonus(self):
        return self.salary * 0.1


manager = Manager("mohammd miri",  "Manager",10000)


employees = [manager, Developer]

for employee in employees:
    print(employee.get_name())
    print(employee.get_bonus())
    print()




# print(manager.salary)