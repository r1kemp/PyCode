# test_numpy

import numpy as np

# na = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(na)
# print(np.shape(na))

# naFlipped = np.flip(na)
# print(naFlipped)

# naReshaped = np.reshape(na, (4,3))
# print(na)
# print(naReshaped)
# na[0] = 11
# print(na)
# print(naReshaped)

# naTransposed = np.transpose(naReshaped)
# print(naTransposed)

# na[1] = 22

# print(na)
# print(naFlipped)
# print(naReshaped)
# print(naTransposed)

# lst = []
# lst.append(map(int, ['1','2','3']))
# lst.append(map(int, ['4','5','6']))
# print(lst)
# na = np.array(lst)
# print(na)


# arr = list(map(int, input().split()))
# print(arr)

# import numpy

# n,m,p = map(int, input().split())

# a1 = [list(map(int, input().split())) for _ in range(n)]
# a2 = [list(map(int, input().split())) for _ in range(m)]

# na1 = numpy.array(a1)
# na2 = numpy.array(a2)
# print(na1)
# print(na2)

# na3 = numpy.concatenate((na1, na2), axis = 1)

# print(na3)

import numpy

# nums = list(map(int, input().split()))

# for i in range(len(nums)):
#     print(numpy.zeros((nums[i], nums[i]), dtype = numpy.int))
#     if i != len(nums) - 1:
#         print()

# for i in range(len(nums)):
#     print(numpy.ones((nums[i], nums[i]), dtype = numpy.int))
#     if i != len(nums) - 1:
#         print()


# nums = tuple(map(int, input().split()))
# print (numpy.zeros(nums, dtype = numpy.int))
# print (numpy.ones(nums, dtype = numpy.int))

# print(numpy.identity(5, dtype = numpy.int))
# r = 5
# c = 6
# print(numpy.eye(r, c, dtype = numpy.int, k=2))
# print(numpy.eye(r, c, dtype = numpy.int, k=1))
# print(numpy.eye(r, c, dtype = numpy.int))
# print(numpy.eye(r, c, dtype = numpy.int, k=-1))
# print(numpy.eye(r, c, dtype = numpy.int, k=-2))


# n,m = map(int, input().split())
# A = []
# B = []
# if n == 1:
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
# else:
#     A = [list(map(int, input().split())) for _ in range(n)]
#     B = [list(map(int, input().split())) for _ in range(n)]

# A = numpy.array(A, dtype = numpy.int)
# B = numpy.array(B, dtype = numpy.int)
# print(A)
# print(B)
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)
# print(A ** B)

'''
    numpy: floor, ceil, rint
'''
import numpy
# numpy.set_printoptions(sign=' ')

# A = numpy.array(list(map(float, input().split())))

# print(numpy.floor(A))
# print(numpy.ceil(A))
# print(numpy.rint(A))

'''
    numpy: sum, prod
'''

# n, m = map(int, input().split())

# A = numpy.array([list(map(int, input().split())) for _ in range(n) ])

# sumA = numpy.sum(A, axis = 0)
# prodOfSumA = numpy.prod(sumA)

# print(sumA)
# print(prodOfSumA)

'''
    numpy: min, max
'''
# n,m = map(int, input().split())

# A = numpy.array([list(map(int, input().split())) for _ in range(n)])

# minA = numpy.min(A, axis = 1)
# maxOfMinA = numpy.max(minA)

# print(maxOfMinA)

'''
    numpy: mean, var, std
'''

# n,m = map(int, input().split())

# A = numpy.array([list(map(int, input().split())) for _ in range(n)])

# print(numpy.mean(A, axis = 1))
# print(numpy.var(A, axis = 0))
# print(numpy.std(A, axis = None))

'''
    numpy: matmul, dot
'''
# n = int(input())

# A = numpy.array([list(map(int, input().split())) for _ in range(n)])
# B = numpy.array([list(map(int, input().split())) for _ in range(n)])
# print(A)
# print(B)
# C = numpy.matmul(A, B)
# print(C)
# C = numpy.dot(A, B)
# print(C)

'''
    numpy: inner and outer product
'''
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# print(numpy.inner(A, B))
# print(numpy.outer(A, B))

'''
numpy polynomial functions:

poly:       returns the coefficients of a polynomial with the given sequence of roots
roots:      returns the roots of a polynomial with the given coefficients
polyint:    returns an antiderivative (indefinite integral) of a polynomial
polyder:    returns the derivative of the specified order of a polynomial
polyval:    evaluates the polynomial at specific value
polyfit:    fits a polynomial of a specified order to a set of data using a least-squares approach

TODO: try out the above poly... functions
'''

'''
numpy: linear algebra
'''

n = int(input())
A = [list(map(float, input().split())) for _ in range(n)]

valOfDet = numpy.linalg.det(A)
print('{0:.2f}'.format(valOfDet))
print(numpy.linalg.eig(A))

aInv = numpy.linalg.inv(A)
print(aInv)

print(numpy.matmul(A, aInv))
