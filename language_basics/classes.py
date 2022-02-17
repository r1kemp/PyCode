class MyClass:
    x = 5
    y = 6

print(MyClass.x)
print(MyClass.y)

del MyClass.y
# print(MyClass.y)

MyClass.z = 9
print(MyClass.z)

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
print(dir(p1))

# delete an attribute
print('deleting age ...')
del p1.age
print(dir(p1))

#delete the object
try:
   del p1
   print(p1)  # this will throw an exception
   print(dir(p1))
except Exception as e:
    print('Exception:', e)
# except NameError:
#    print("NameError: name 'p1' is not defined")

p1 = None
print(p1)


'''
        INHERITANCE

'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

#   def __str__(self):
#     return f'{self.firstname} {self.lastname}'

  def __repr__(self) -> str:
    return f'{self.firstname} {self.lastname}'

class Student(Person):
  def __init__(self, fname, lname, gyear):
    super().__init__(fname, lname)
    self.graduationyear = gyear

#   def __str__(self):
#     return f'{str(super())} {self.graduationyear}'
#     # return f'{super().__str__()} {self.graduationyear}'

  def __repr__(self):
    return f'{super().__repr__()} {self.graduationyear}'

x = Student("Mike", "Olsen", 2019)
print(str(x))