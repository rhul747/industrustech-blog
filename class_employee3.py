class Person:
def init (self,a,b):

self.name=a

self.age=b
class Employee (Person)
def __init__(self,a,b,id,salary):

super().__init(a,b)
self.id=id

self.salary=salary
def show(self):

print("name:",self.name,"/nage:",self.age,"/nempd: ",self.id,"/nsalary: ",self.salarary)
e=Employee("elwin",25,350,25035000)
e.show()
