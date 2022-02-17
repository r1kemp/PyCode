# test
import random

N = 4
K = 3
P = 5
print('1')
print(f'{N} {K} {P}')

for _ in range(N):
    lst = random.sample(range(10, 20), K)
    print(*lst)