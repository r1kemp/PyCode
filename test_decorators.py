# test_decorators.py

def printCentered(title):
    print(title.center(52, '-'))

# g_string = "a global string"
# g_val = 2

# def foo():
#     g_string = "value changed"
#     xyzzzzzzzzzzz = 66
#     print('-------------locals------------------')
#     print(locals())
#     print('===============================')

# foo()

# print('--------------globals-----------------')
# print(globals())
# print('===============================')

# print('Example of __call__ in a class'.center(52, '-'))
printCentered('Example of __call__ in a class')

class add(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, a, b):
        return a + b
    def sum2(self):
        return self.a + self.b

x = add(2, 6)
print(x.sum2())

y = x(1, 9)     # this calls the __call__ method
print(y)

printCentered('myDecorator class')
class myDecorator(object):
    def __init__(self, f):
        print( "inside myDecorator.__init__()")
        self.f = f
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside myDecorator.__call__()")
        #self.f()

@myDecorator
def aFunction():
    print("inside aFunction()")

print( "Finished decorating aFunction()")

aFunction()

'''
A Better Example
'''
printCentered('A Better Example of decorator class'.center(52, '-'))

class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print( "Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entryExit
def func1():
    print("inside func1()")

@entryExit
def func2():
    print("inside func2()")

func1()
func2()
# print(func1.__str__)

printCentered('Function decorator')

def entryExit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
        
    new_f.__name__ = f.__name__
    return new_f

@entryExit
def func1():
    print('inside func1()')

@entryExit
def func2():
    print('inside func2()')    

func1()
func2()
print(func1.__name__)
print(func2.__name__)