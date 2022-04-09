ri = lambda: int(input())

ris = lambda: (int(x) for x in input().split(' '))
'''
>>> a, b, c = ris()
2 6 1
>>> a
2
>>> b
6
'''
