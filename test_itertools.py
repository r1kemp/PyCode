# test_itertools

# import itertools

# counter = itertools.count(start = 5, step=0.5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400, 500]
# dd = zip(itertools.count(), data)
# # print(next(dd))
# # print(next(dd))
# # print(next(dd))
# print(list(dd))

# from itertools import product
# A = [int(e) for e in input().split(' ')]
# B = map(int, input().split())
# # print(*A)
# # print(*B)
# # C = [(a, b) for a in A for b in B]
# # print(*C)

# # C = []
# # for a in A:
# #     for b in B:
# #         C.append(tuple((a, b)))

# # print(*C)
# print(*list(product(A, B)))

# from itertools import permutations
# S, n = input().split()
# S = sorted(S)
# # print(S)
# for e in permutations(S, int(n)):
#     print(''.join(e))

# from itertools import combinations
# S, n = input().split()
# S = sorted(S)
# n = int(n)
# for i in range(1, n+1):
#     for e in combinations(S, i):
#         print(''.join(e))

# from itertools import combinations_with_replacement
# S, n = input().split()
# S = sorted(S)
# n = int(n)
# for e in combinations_with_replacement(S, n):
#     print(''.join(e))

# from itertools import count

# from collections import Counter
# def comb(n, k):
#     num = 1
#     for f in range(n, n-k, -1):
#         num *= f
#     den = 1
#     for f in range(1, k+1):
#         den *= f
#     return num / den

# N = int(input())
# A = input().count('a')
# K = int(input())

# num = comb(N-A, K)
# den = comb(N, K)
# p = 1.0 - num/float(den)
# print(round(p,3))

