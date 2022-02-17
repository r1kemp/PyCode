mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

try:
   print(next(myit)) # thi line will throw StopIteration
except Exception as e:
   print("EXCEPTION: ", type(e), e.__repr__())

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    if x == 9: raise StopIteration
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

myclass2 = MyNumbers()
for x in myclass2:
  print(x)

import dicts
print(dir(dicts))