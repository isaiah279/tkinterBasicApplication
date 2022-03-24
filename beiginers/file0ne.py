"""import mysql.connector
import  tkinter
mydb = mysql.connector.connect(user="root", host="localhost", password="", database="companyy")

mycursor = mydb.cursor()

mycursor.execute("describe registration")
for db in mycursor:
    print(db)"""
""" 

class Myclass:
    "this is my class"
  

  def fun(self):
        print('hello')

    def mathematisc(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        m = x ** (y * z)
        return m


obj = Myclass()

print(obj.fun())
f = obj.mathematisc(int(input("enter x")), int(input("enter y:")), int(input("enter z:")))
print(f)
# OBJETCS cna be used to creast new objects and acces may place of the codes
"""

'''
class CompleNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.image = i

    def getData(self):
        print('{0}+{1}'.format(self.real, self.image))
        # creataing anew complexity number object


c1 = CompleNumber(2, 3)
print(c1)
c1.getData()

# creating another Complexnumber object
# and create a new a tribute

c2 = CompleNumber(5)
c2.getData()
c2.attr = 10
print((c2.real, c2.image, c2.attr))
del c1.attr
c1.getData()'''

"""class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("tim", 34)
d.set_age(23)
print(d.name)
dog_name = ["time", "kick"]
"""

'''
class Student:
    def __init__(self, name, age, grade):
        # attributes
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    # newclass to add srudent to a course


class Course:
    def __init__(self, name, max_studens):
        self.name = name
        self.max_students = max_studens
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_aver_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student(input("enter name"),int(input('ente number')),int(input("enter name:")))
s2 = Student("Bill", 19, 75)
s3 = Student("jill", 34, 45)
course = Course("science", 200)
course.add_students(s1)
course.add_students(s2)
mm = course.add_students(s1)
print(course.get_aver_grade())'''


# INHERITANCE

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")


# self.name is a variable container
class Cat(Pet):
    def speak(self):
        print("barking")


p = Pet("Tim", 19)
p.show()
c=Cat("bill",34)
c.show()