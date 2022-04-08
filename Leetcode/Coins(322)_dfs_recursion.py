
# Coins

from audioop import reverse
from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins, amount) -> int:
        coins.sort()
        self.coins = coins
        self.inf = 9999999

        ans = self.dp(amount)
        return ans if ans != self.inf else -1
    
    @cache
    def dp(self, remAmt):
        if not remAmt: return 0
        if remAmt < self.coins[0]: return self.inf

        count = self.inf
        for coin in self.coins:
            if coin > remAmt: break
            thisCount = self.dp(remAmt - coin) + 1
            count = min(count, thisCount)

        return count

        
test_data = [
    {'coins':[1,2,5], 'amt': 4, 'ans': 2},
    {'coins':[1], 'amt': 0, 'ans': 0},
    {'coins':[3,5], 'amt': 0, 'ans': 0},
    {'coins':[3,5], 'amt': 2, 'ans': -1},
    {'coins':[3,5], 'amt': 3, 'ans': 1},
    {'coins':[3,5], 'amt': 4, 'ans': -1},
    {'coins':[3,5], 'amt': 5, 'ans': 1},
    {'coins':[3,5], 'amt': 6, 'ans': 2},
    {'coins':[3,5], 'amt': 7, 'ans': -1},
    {'coins':[3,5], 'amt': 8, 'ans': 2},
    {'coins':[3,5], 'amt': 9, 'ans': 3},
    {'coins':[3,4,1,5], 'amt': 7, 'ans': 2},
    {'coins':[3,4,1,5], 'amt': 9, 'ans': 2},
    {'coins':[3,4,1,5], 'amt': 12, 'ans': 3},
    {'coins':[346,29,395,188,155,109], 'amt': 9401, 'ans':26},
    # {'coins':[2,4,6,8,10,12,14,16,18,20,22,24], 'amt': 9999, 'ans': -1},
    {'coins':[186,419,83,408], 'amt': 6249, 'ans': 20}
]

for i, data in enumerate(test_data, start=1):
    s = Solution()
    ans = s.coinChange(data['coins'], data['amt'])
    if ans == data['ans']:
        print(f'Test #{i} passed!!')
    else:
        print(f'Test #{i} FAILED********')
