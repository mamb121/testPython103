import math
import random
import datetime
import Student

#my_name = input('Entry your name :')
#print('Hello',my_name)

name ='Fatimah'
age = 45
is_marreid = True
driving_license = None

print(type(driving_license))

float_number = float(age)
print(float_number)

names = ['as','dd','ss']
print(names[2])
names[2] = 'sdadasdada'
print(names[2])
names.append('sds')
print(names)
names.insert(0,'24243')
print(names)
names.remove('24243')
print(names)

child_one =('ahmed','Riyadh','1-1-2024')
print(type(child_one))
print(child_one)

child_two = {'name':'Ahmed','city':'Riyadh','birhdate':'-1-2000','age':29}
print(child_two)
print(type(child_two))
print(child_two['city'])
print(child_two.values())
print(child_two.keys())

age = 18
if age >18:
    print('you are an adult')
elif age == 18:
    print('ues')
else:
    print('no')

i=1

while i<=5:
    print(i)
    i += 1

for i in range(4):
    print(i)

def print_numbers(to):
    for i in range(to):
        print(i)

print_numbers(5)

def add(f,s):
    print(f+s)

add(2,44)

def adds(f,s):
    return f+s

vv= adds(23,44)
print(vv)
print("ssss")
def multiplication(number):
    print('Multiplication result:')
    return number * number


print(multiplication(2))

numbers = 100,121,134,1354
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(pow(2,3))
print(math.sqrt(144))
print(math.remainder(26,5))


print(random.randint(1,100))

fsyr = datetime.date(2024,2,29)
print(fsyr)

timenow = datetime.datetime.today()
print(timenow)
print(timenow.day)
print(timenow.second)
print(timenow.strftime('%A %B %Y'))

alphabet ='abcdefghijklmnopqrstuqvwxyz'
habet ='abcdefghijklm'
print(alphabet[5:18:2])
print('x' in alphabet)
print(habet*2 + ' ' + alphabet)

grade = 'Fail'
if "Fail" not in grade:
   print('Congratulations, you have passed the exam!')
else:
   print('Sorry, you have failed the exam.')

print(alphabet.find('s'))
text = ('a','l','i')
print(''.join(text))

values = [1,True,'Python']
print(values[2])
values = [[1,2,3]
         ,[4,5,6]
         ,[7,8,9]]
print(values[2][2])
