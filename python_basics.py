# python_basics

# integer_list = map(int, input().split(','))
# print(integer_list)
# lst = list(integer_list)
# print(lst)
# print(tuple(lst))

# if __name__ == '__main__':
#     N = int(input())
#     the_lst = []
#     for _ in range(N):
#         cmd = [e for e in input().split()]
#         if cmd[0] == 'insert':
#             e = int(cmd[2])
#             i = int(cmd[1])
#             the_lst.insert(i, e)
#         elif cmd[0] == 'remove':
#             the_lst.remove(int(cmd[1]))
#         elif cmd[0] == 'append':
#             the_lst.append(int(cmd[1]))
#         elif cmd[0] == 'sort':
#             the_lst = sorted(the_lst)
#         elif cmd[0] == 'reverse':
#             the_lst.reverse()
#         elif cmd[0] == 'print':
#             print(the_lst)

# if __name__ == '__main__':
#     allScores = []
#     unique_scores = set()
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         allScores.append((name, score))
#         unique_scores.add(score)

#     unique_scores = sorted(list(unique_scores))
#     seconds = [e[0] for e in allScores if e[1] == unique_scores[1]]
#     seconds = sorted(seconds)
#     for n in seconds:
#         print(n)

# allScores = [(input(), float(input())) for _ in range(int(input()))]
# unique_scores = sorted(set(e[1] for e in allScores))
# seconds = [e[0] for e in allScores if e[1] == unique_scores[1]]
# for name in sorted(seconds):
#     print(name)

# # to print 25.2 as 25.20
# avg = 25.2
# print('{:0.2f}\n'.format(avg))

# name, *line = input().split()
# print(name, line)

# S = 'aBCde 345 pQR'
# print(S.swapcase())

# def count_substring(string, sub_string):
#     count = 0
#     index = string.find(sub_string)
#     while index >= 0:
#         count += 1
#         string = string[index+1:]
#         index = string.find(sub_string)

#     return count
     

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# S, N = input(), int(input())
N = 3
# S = 'AABCAAADA'
# lst = [iter(S)] * N
# print(lst)
# for part in zip(*[iter(S)] * N):
#     print(part)

# def setd(d, c):
#     d[c] = c
#     return c

# def print_uc(string):
#     d = dict()
#     lst = [setd(d, c) for c in string if c not in d]
#     print(''.join(lst))

#     # for c in string: 
#     #     if c not in d:
#     #         d[c] = c
#     # print(''.join(d))
#     # d = dict()
#     # print(''.join([ d.setdefault(c, c) for c in string if c not in d ]))

# def merge_the_tools(S, ll):
#     n = len(string)
#     k = int(n / ll)
#     index = 0
#     for _ in range(k):
#         print_uc(string[index : (index + ll)])
#         index += ll

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

# A = set(input().split())
# n = int(input())
# AllBs = [set(input().split()) for _ in range(n)]
# print(all(map(lambda x: A > x, AllBs)))

# print(all([True, True, False]))

# a, b = int(input()), int(input())
# a, b = 1, 10
# import math
# theta = math.atan(a/b)
# theta = int(round(math.degrees(theta)))
# degree_sign = u"\N{DEGREE SIGN}"
# print(str(theta) + degree_sign)

'''
collections.defaultdict
'''

# from collections import defaultdict
# d = defaultdict(list)

# n, m = map(int, input().split())
# for i in range(n):
#     d[input()].append(i + 1)
# for _ in range(m):
#     c = input()
#     if c in d:
#         print(*d[c])
#     else:
#         print(-1)

'''
collections.namedtuple
'''

# from collections import namedtuple

# n = int(input())
# header = input().split()
# Student = namedtuple('Student', header)
# total = 0
# for _ in range(n):
#     s = Student._make(input().split())
#     total += int(s.MARKS)
# print('{0:.2f}'.format(total / n))

'''
collections.OrderedDict
'''

#from collections import OrderedDict

# d = dict()
# n = int(input())
# for _ in range(n):
#     item, space, qty = input().rpartition(' ')
#     if item in d:
#         d[item] += int(qty)
#     else:
#         d[item] = int(qty)
# for item in d.items():
#     print(*item)




'''
collections.deque
'''
# from collections import deque
# d = deque()
# n = int(input())
# print(*d)


'''
Calendar
'''
# import calendar
# print('calendar.weekday(2020, 5, 22) =', calendar.weekday(2020, 5, 22))
# print(list(calendar.month_name)[8])
# print(list(calendar.day_name))
# print(list(calendar.day_name)[calendar.weekday(2015, 8, 5)].upper())

'''
Exception
'''
# for i in range(int(input())):
#     try:
#         a,b=map(int,input().split())
#         print(a//b)
#     except Exception as e:
#         print("Error Code:",e)

'''
Regular expression
'''
# import re
# for _ in range(int(input())):
#     ans = True
#     try:
#         reg = re.compile(input())
#     except re.error:
#         ans = False
#     print(ans)

# S = 'WELCOME'
# T = S.center(21, '-')
# print(T)
# pat1 = '.|.'
# pat5 = pat1 * 5
# print(pat5)

'''
    string.center(width, '-')
'''

# size, width = map(int, input().split())
# pat = '.|.'
# m = size // 2
# for i in range(m):
#     numPats = 2 * i + 1
#     curr_pat = pat * numPats
#     print(curr_pat.center(width, '-'))

# print('WELCOME'.center(width, '-'))

# for i in range(m+1, size):
#     numPats = (size - i - 1) * 2 + 1
#     curr_pat = pat * numPats
#     print(curr_pat.center(width, '-'))


'''
    datetime
'''
# def time_delta(t1, t2):  This doesn't work
#     ts1 = t1.split()
#     ts2 = t2.split()
#     h1, m1, s1 = map(int, ts1[4].split(':'))
#     h2, m2, s2 = map(int, ts2[4].split(':'))
#     timeZoneDiff_1 = int(ts1[5])
#     timeZoneDiff_2 = int(ts2[5])

#     h1 += timeZoneDiff_1 // 100
#     m1 += timeZoneDiff_1 % 100

#     h2 += timeZoneDiff_2 // 100
#     m2 += timeZoneDiff_2 % 100

#     delta = (h2 - h1) * 60 + (m2 -m1)
#     delta = delta * 60 + (s2 - s1)

#     return delta

# from datetime import datetime as dt

# fmt = '%a %d %b %Y %H:%M:%S %z'
# # for i in range(int(input())):
# #     print(int(abs((dt.strptime(input(), fmt) - 
# #                 dt.strptime(input(), fmt)).total_seconds())))

# wit1 = dt.strptime('Sun 10 May 2015 13:54:36 -0700', fmt)
# print(wit1)
# wit2 = dt.strptime('Sun 10 May 2015 13:54:36 -0000', fmt)
# print(wit2)

# diff = (wit1 - wit2).total_seconds()
# print(diff)


# T = int(input())
# for _ in range(T):
#     t1 = input()
#     t2 = input()
#     delta = time_delta(t1, t2)
#     print(delta)

'''
Regular Expression
'''
# import re
# pattern = '^[+-]?[0-9]*\.[0-9]+$' 

# def match(mathExp):
#     rematchObj = re.match(pattern, mathExp)
#     print(mathExp, ' --> ', rematchObj)

# es = ['+4.50', '-1.0', '.5', '-.7', '+.4', '-+4.5']
# for e in es:
#     match(e)

# rematchObj = re.match(pattern, '3.54')
# print(rematchObj.span())
# rematchObj = re.match(pattern, '3.5A4')
# print(rematchObj)

# import re
# S = '...23451672213567123'
# m = re.search(r'([a-zA-Z0-9])\1+', S.strip())
# print(m.group(1) if m else -1)

N, k = input()
# K = input()
name = input()
print(str(N) + " " + name)
# print(name)