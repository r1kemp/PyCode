# test_collections

# from collections import Counter #, namedtuple, OrderedDict, defaultdict, deque

# a = 'bbbaacddddee'
# my_counter = Counter(a)
# # print(my_counter.items())
# # print(my_counter.keys())
# # print(my_counter.values())
# # print(*list(my_counter.values()))
# # print(my_counter.most_common(1))
# # print(my_counter.most_common(1)[0][0])

# adict = {'a':5, 'b':8, 'g':9}
# # print(adict.keys())
# # print(list(adict.values()))
# # print(*list(adict.values()))

# from collections import namedtuple as nt
# # Point = nt('Point', 'x, y')
# # pt = Point(1, 5)
# # print(pt)
# # print(pt.x, pt.y)

# from collections import defaultdict
# # d = defaultdict(list)
# # d['a'] = 100
# # d['b'] = 200
# # print(d['a'])
# # print(d['ccc'])

# from collections import deque
# d = deque()
# d.append(2)
# d.append(3)
# print(d)
# d.appendleft(1)
# print(d)
# print(d.pop())
# print(d)
# print(d.popleft())
# print(d)
# d.clear()
# print(d)

# from collections import Counter
# s = 'ccbbbaade'
# myCounter = Counter(s)
# mc3 = myCounter.most_common(3)
# mc3 = sorted(mc3, key =lambda x: x[0])
# mc3 = sorted(mc3, key =lambda x: x[1], reverse = True)
# # print(mc3)
# for t in mc3:
#     print(t[0], t[1])

from collections import Counter
def method_counter():
    myCounter = Counter(input())
    mc3 = myCounter.most_common()
    mc3 = sorted(mc3, key =lambda x: (-x[1],x[0]))
    # mc3 = sorted(mc3, key =lambda x: x[0])
    # mc3 = sorted(mc3, key =lambda x: x[1], reverse = True)
    mc3 = mc3[:3]
    for t in mc3:
        print(t[0], t[1])

def method_raw(S):
    # S = raw_input()
    # S = input()
    letters = [0]*26

    for letter in S:
        letters[ord(letter)-ord('a')] += 1

    for _ in range(3):
        
        max_letter = max(letters)
        
        for index in range(26):
            if max_letter == letters[index]:
                print(chr(ord('a')+index), max_letter)
                letters[index] = -1
                break    

# method_raw('bbcccddefaa')
# bbcccddefaa

# import array
# ia = array.array('l', [3,7,12])
# # ia.append(3)
# # ia.append(7)
# ia.append(15)
# print(ia)
# ia[1] += 10
# print(ia)

# import numpy as np
# A = np.array([0]*10)
# print(A)
# A[2] += 3
# print(A)
# B = np.zeros(10, dtype = np.int32)
# print(B)

# import numpy as np
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     na = np.array([0]*n)
#     line = input()
#     sa = line.split(' ')
#     for i in range(n):
#         na[i] = int(sa[i])
#     l = 0
#     r = n-1
#     curr_length = max(na[0], na[n-1])
#     success = True
#     while l < r:
#         index = -1
#         if na[l] >= na[r]:
#             index = l
#             l += 1
#         else:
#             index = r
#             r -= 1

#         if na[index] > curr_length:
#             success = False
#             break

#         curr_length = na[index]

#     print('YES' if success else 'NO')


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     na = [0]*n
#     line = input()
#     sa = line.split(' ')
#     for i in range(n):
#         na[i] = int(sa[i])
#     l = 0
#     r = n-1
#     curr_length = max(na[0], na[n-1])
#     success = True
#     while l < r:
#         index = -1
#         if na[l] >= na[r]:
#             index = l
#             l += 1
#         else:
#             index = r
#             r -= 1

#         if na[index] > curr_length:
#             success = False
#             break

#         curr_length = na[index]

#     print('Yes' if success else 'No')

# from collections import deque    
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     dq = deque()
#     line = input()
#     sa = line.split(' ')
#     for i in range(n):
#         dq.append(int(sa[i]))
    
    
#     success = True
#     left = dq.popleft()
#     right = dq.pop()
#     curr_length = max(left, right)
#     while len(dq) > 0:
#         if left >= right:
#             if left > curr_length:
#                 success = False
#                 break
#             else:
#                 curr_length = left
#                 left = dq.popleft()
#         else:
#             if right > curr_length:
#                 success = False
#                 break
#             else:
#                 curr_length = right
#                 right = dq.pop()
            
#     if success:
#         success = curr_length >= left and curr_length >= right

#     print('Yes' if success else 'No')
print('===========================================')
x = map(len, ('app', 'banana', 'mango'))
print('x =', list(x))

y = map(int, '123158491')
print(list(y))

print('===========================================')
from itertools import groupby
for k, g in groupby("1222311"):
    print(tuple([len(list(g)), int(k)]), end = ' ')
    # print('(' + str(len(list(g))) + ', ' + str(k) + ')', end = ' ')
    