class Vehicle:
    def __init__(self, company, owner, color, current_speed):
        self.company = company
        self.owner = owner
        self.color = color
        self.current_speed = current_speed

    def move(self):
        print('the car has moved')

    def stop(self):
        print('the car has stopped')

class Car(Vehicle):
    def display(self):
        print('this is class car')


car1 = Car('Nissan', 'ahmed', 'blue', 25)

