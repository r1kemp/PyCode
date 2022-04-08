from collections import deque
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        coins.sort()

        queue = deque([(amount, 0)])
        visited = { amount }

        def children(val):
            for coin in coins: yield val - coin

        while queue:
            remAmt, depth = queue.popleft()
            for child in children(remAmt):
                if child in visited: continue
                if not child: return depth + 1
                if child < 0: break
                visited.add(child)
                queue.append((child, depth+1))
        return -1

        

  
test_data = [
    # {'coins':[1,2,5], 'amt': 4, 'ans': 2},
    # {'coins':[1], 'amt': 0, 'ans': 0},
    # {'coins':[3,5], 'amt': 0, 'ans': 0},
    # {'coins':[3,5], 'amt': 2, 'ans': -1},
    # {'coins':[3,5], 'amt': 3, 'ans': 1},
    # {'coins':[3,5], 'amt': 4, 'ans': -1},
    # {'coins':[3,5], 'amt': 5, 'ans': 1},
    # {'coins':[3,5], 'amt': 6, 'ans': 2},
    # {'coins':[3,5], 'amt': 7, 'ans': -1},
    # {'coins':[3,5], 'amt': 8, 'ans': 2},
    # {'coins':[3,5], 'amt': 9, 'ans': 3},
    # {'coins':[3,4,1,5], 'amt': 7, 'ans': 2},
    # {'coins':[3,4,1,5], 'amt': 9, 'ans': 2},
    # {'coins':[3,4,1,5], 'amt': 12, 'ans': 3},
    # {'coins':[346,29,395,188,155,109], 'amt': 9401, 'ans':26},
    # {'coins':[2,4,6,8,10,12,14,16,18,20,22,24], 'amt': 9999, 'ans': -1},
    {'coins':[3,7,12,9], 'amt': 432, 'ans': 6},
    {'coins':[186,419,83,408], 'amt': 6249, 'ans': 20},
]

for i, data in enumerate(test_data, start=1):
    s = Solution()
    ans = s.coinChange(data['coins'], data['amt'])
    if ans == data['ans']:
        print(f'Test #{i} passed!!')
    else:
        print(f'Test #{i} FAILED********')
        print(f'Expected {data["ans"]}, got {ans}')


















'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0):return 0
        qs = [amount]
        visited = set([amount])
        change = 0
        while qs:
            next_qs = []
            for q in qs:
                for c in coins:
                    if(q>c and q-c not in visited ):
                        next_qs+=[q-c]
                        visited.add(q-c)
                    elif(q==c):
                        return change+1
            change+=1
            qs = next_qs
        return -1
'''        