# def times(by = None):
#    def multiply_res_dec(fun):

def times(by = None):
    def multiply_real_decorator(function):
        def wrapper(*args,**kwargs):
            return by * function(*args,**kwargs)
        return wrapper
    return multiply_real_decorator

@times(3)
def adder(a,b):
  return a + b

print(adder(2,3))

