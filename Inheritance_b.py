class Person():
    def __init__(self ,first_name ,surname ,tel):
        self.first_name = first_name
        self.surname = surname
        self.tel = tel
    def full_name(self):
        return self.first_name + " " + self.surname

class Employee(Person):
    salary = 0.0
    def __init__(self,first_name ,surname ,tel,salary):
        Person.__init__(self ,first_name ,surname ,tel)
        self.salary = salary

    def give_raise(self,amount):
        self.salary =  self.salary + amount

dd = Employee("","",154,5000)
dd.give_raise(200)
print(dd.salary)