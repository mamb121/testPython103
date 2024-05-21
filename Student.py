class Student:
    university_name ='King saud uninversity'

    def set_university_name(self, value):
        self.university_name = value

    def get_university_name(self):
         return self.university_name

    def __init__(self, name, age, id, grades):
        self.name = name
        self.age = age
        self.id = id
        self.grades = grades

    def talk(self):
        print('My name is : ', self.name)


stud1 = Student('ali', 34, '213232', 22)
print('-------')
stud2 = Student('omar', 30, '213232', 22)
print('-------')
stud1.talk()
print('-------')
stud2.talk()
print('-------')
stud2.v_hours = 25
print(dir(stud1))
print('-------')
print(dir(stud2))
print('-------')
del stud2.v_hours
print(dir(stud2))
print('-------')
print(stud1.university_name)
print(stud2.university_name)
print('-------')
stud2.set_university_name('KAAU')
print('-------')

print(stud1.university_name)
print(stud2.university_name)