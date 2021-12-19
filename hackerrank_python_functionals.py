# hackerrank_python_functionals

'''
    list, range, map, filter
'''

# l = list(range(10))
# print(l)
# # l = list(map(lambda x: x**2, l))
# # print(l)
# # l = list(filter(lambda x: x > 10 and x < 80, l))
# # print(l)

# # sqr = lambda x: x**2
# # l = list(map(sqr, l))
# # print(l)

# # _10to80 = lambda x: x > 10 and x < 80
# # l = list(filter(_10to80, l))
# # print(l)

# def sqr(x): return x**2
# l = list(map(sqr, l))
# print(l)

# def _10to80(x): return x > 10 and x < 80
# l = list(filter(_10to80, l))
# print(l)


'''
    split(), rsplit(), isalnum()
'''

# def fun(s):
#     # return True if s is a valid email, else return False

#     s = s.split('@')
#     if len(s) != 2 or len(s[0]) == 0:
#         return False
    
#     # The username can only contain letters, digits, dashes and underscores
#     for c in s[0]:
#         if not (c.isalnum() or c == '_' or c == '-'):
#             return False
    
#     s = s[1].rsplit('.')
#     if len(s) != 2:
#         return False

#     for c in s[0]:
#         if not c.isalnum():
#             return False
    
#     if len(s[1]) > 3:
#         return False
        
#     return True
    

# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

'''
    functools.reduce()
'''
# from functools import reduce
# from math import gcd

# res = reduce(lambda x, y: x + y, [1,2,3])
# print(res)

# res = reduce(lambda x, y: x + y, [1,2,3], -3)
# print(res)

# res = reduce(gcd, [6, 12, 36])
# print(res)

# res = reduce(gcd, [6, 12, 36], 5)
# print(res)


# from fractions import Fraction
# f1 = Fraction(6, 10)
# print(f1)

# f2 = Fraction(6, 21)
# print(f2)

# f3 = f1 * f2
# print(f3)

# print(f1 / f2)


# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
        
#     def __add__(self, no):
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)

#     def __sub__(self, no):
#         return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
#     def __mul__(self, no):
#         a, b = self.real, self.imaginary
#         c, d = no.real, no.imaginary
#         return Complex(a*c - b*d, b*c + a*d)

#     def __truediv__(self, no):
#         a, b = self.real, self.imaginary
#         c, d = no.real, no.imaginary
#         den = c**2 + d**2
#         real = (a*c + b*d) / den
#         imag = (b*c - a*d) / den
#         return Complex(real, imag)

#     def mod(self):
#         return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


'''
    zip([iterabe1, iterable2, ...])
    zip generates tuples. The ith tuple contains the ith element from each of the iterables
'''
# N, X = map(int, input().split())
# S = []
# for _ in range(X):
#     s = list(map(int, input().split()))
#     S.append(s)
# lst = list(zip(*S))
# for st in lst:
#     print('{0:.1f}'.format(sum(st) / X))

# def gen_sqrs(start = 1):
#     while True:
#         yield start**2
#         start += 1

# def gen_cubes(start = 1):
#     while True:
#         yield start**3
#         start += 1

# print(list(zip([1,2,3,4,5,6], gen_sqrs(), gen_cubes())))

# x, k = map(int, input().split())
# exp = input().split('+')
# lsum  = 0
# for e in exp:
#     e = e.strip()
#     e2 = e.split('-')

#     if '**' in e:
#         left, star, n = e.rsplit('*')
#         n = int(n)
#         lsum += x**n
#     elif e == 'x':
#         lsum += x
#     elif e.isdigit():
#         lsum += int(e)
# print('True' if lsum == k else 'False')

# x, k = map(int, input().split())
# print(eval(input()) == k)

# def ispal(s):
#     s = str(s)
#     l, r = 0, len(s)-1
#     while l < r: 
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

'''
Reverse a string
'''
# x = 'abcde'
# print(x[::-1]) # x[::-] reverses the string!!!

'''
    sorted
    https://www.hackerrank.com/challenges/ginorts/problem
'''
# S = 'Sorting1234' #input()
# lower = ''.join(sorted(list(e for e in S if e.islower())))
# upper = ''.join(sorted(list(e for e in S if e.isupper())))
# digits = ''.join(sorted(list(e for e in S if e.isdigit()), key = lambda x: '1357902468'.index(x)))
# print(lower + upper + digits)

'''
    decorators
    https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
'''
# def wrapper(f):
#     def fun(l):
#         l = ['+91 ' + e[-10:-5] + ' ' + e[-5:] for e in l]
#         f(l)
#     return fun

# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')

# if __name__ == '__main__':
#     l = [input() for _ in range(int(input()))]
#     sort_phone(l) 

'''
more decorator
'''
# import operator

# def person_lister(f):
#     def inner(people):
#         # people = sorted(people, key = lambda x: x[2])
#         people = sorted(people, key = lambda x: int(x[2]))
#         people2 = []
#         for person in people:
#             people2.append(f(person))
#         return people2
#     return inner

# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')

'''
XML
'''
# import sys
# import xml.etree.ElementTree as etree

# def get_attr_number(node):
#     print(node.attrib)
#     count = len(node.attrib)
#     for cn in node:
#         count += get_attr_number(cn)

#     return count

# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))

'''
strings print all columns of same width
'''

# def print_formatted(number):
#     w = len("{0:b}".format(n))
#     for i in range(1,n+1):
#         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=w))


# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# def solve(s):
#     for x in s[:].split():
#         s = s.replace(x, x.capitalize())    
#     return s
# print(solve(input()))

# def print_rangoli(size):
#     len = 4 * size - 3
#     rows = [[]]*size

#     first_char = chr(ord('a') + size - 1)
#     prev_char = lambda x: chr(ord(x) - 1)
#     next_char = lambda x: chr(ord(x) + 1)


#     iMid = len // 2
#     for i in range(size):
#         rows[i] = ['-']*len
#         curr_char = first_char
#         for j in range(i+1):
#             rows[i][iMid - j*2] = curr_char
#             rows[i][iMid + j*2] = curr_char
#             curr_char = next_char(curr_char)
#         first_char = prev_char(first_char)

#     for r in rows:
#         print(''.join(r))
#     for i in range(size-2, -1, -1):
#         print(''.join(rows[i]))


# print_rangoli(5)

# char_set = list(chr(ord('a') + 2 - x) for x in range(3))
# s = '-'.join(char_set)
# alpha = s + s[::-1][1:]
# print(alpha.center(17, '-'))
# print(alpha.center(18, '-'))

# n = 5
# for i in range(n):
#     s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
#     print((s+s[::-1][1:]).center(n*4-3, '-'))

# for i in range(n-1):
#     s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
#     print((s+s[::-1][1:]).center(n*4-3, '-'))