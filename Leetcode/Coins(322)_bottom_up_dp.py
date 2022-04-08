
# Coins

class Solution:
    def coinChange(self, coins, amount) -> int:
        _inf = 9999999
        N = amount + 1
        dp = [_inf]*N
        dp[0] = 0

        for i in range(coins[0], N):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] < _inf else -1

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
    {'coins':[2,4,6,8,10,12,14,16,18,20,22,24], 'amt': 9999, 'ans': -1},
    {'coins':[186,419,83,408], 'amt': 6249, 'ans': 20}
]

for i, data in enumerate(test_data, start=1):
    s = Solution()
    ans = s.coinChange(data['coins'], data['amt'])
    if ans == data['ans']:
        print(f'Test #{i} passed!!')
    else:
        print(f'Test #{i} FAILED********')
