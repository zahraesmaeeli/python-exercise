class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Student(Person):
    def __init__(self,name,age,student_ID):
        super().__init__(name,age)
        self._student_ID = student_ID

    def get_student_ID(self):
        return self.student_ID

    def set_student_ID(self, student_ID):
        self.student_ID = student_ID



student=Student("Ali", 20, 982246)
print(student.get_name())
