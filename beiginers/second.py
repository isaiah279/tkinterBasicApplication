'''number=int(input("Enter name :"))
my_dict = {
    1: "okech",
    2: "okelo",
    3: 23
}
number==my_dict.keys()
if number in my_dict:
    print("yess",number.values())
else:
    print("nop")'''

'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def set_age(self,age,many):
        return self.age

d = Dog("tim", 34)
print(d.get_name())
d2 = Dog("bill", 45)
d3=Dog("okalo",456)
print(d2.get_age())
print(d3.set_age(23))'''


class Population:
    def __init__(self, name, age, county):
        self.name = name
        self.age = age
        self.county =county

    def get_conty(self):
         self.age

    def get_name(self):
       return self.name

    def get_age(self):
        self.age

"""
d1 = Population("gasgas","jsdhj","%d")
print(d1.get_name(878878))
"""
class Students:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]
        self.is_active=False
    def add_students(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
        return False
    def get_average_grade(self):
        pass
s1=Students("tim",950)
s2=Students("nnnn",50)
s3=Students("tm",950)
print(s1.max_students)
print(s2.students)


