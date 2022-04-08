
# Coins



# # all tests passed in 2104 ms
# class Solution:
#     def coinChange(self, coins, amount) -> int:
#         if not amount: return 0

#         coins.sort()
#         if amount < coins[0]: return -1

#         depth_inf = 9999999
#         depth = [depth_inf] * (amount + 1)

#         stack = [(0, 0)]

#         def children(v):
#             for coin in coins: yield v + coin

#         while stack:
#             si = stack.pop()
#             curDepth = si[1] + 1
#             if curDepth >= depth[amount]: continue

#             for amt in children(si[0]):
#                 if amt > amount: continue
#                 if amt == amount:
#                     depth[amount] = curDepth
#                     break
#                 if curDepth >= depth[amt]: continue
#                 depth[amt] = curDepth
#                 stack.append((amt, curDepth))

#         return depth[amount] if depth[amount] < depth_inf else -1


class Solution:
    def coinChange(self, coins, amount) -> int:
        if not amount: return 0

        coins.sort()
        if amount < coins[0]: return -1

        depth_inf = 99999
        height_inf = 77777
        depth = [depth_inf] * (amount + 1)
        height = [height_inf] * (amount + 1)
        height[amount] = 0

        stack = [(0, 0)]

        def children(v):
            for coin in coins: yield v + coin

        while stack:
            si = stack.pop()
            if si[1] < 0:
                if (height[-si[1]] + 1) < height[si[0]]:
                    height[si[0]] = height[-si[1]] + 1
                continue

            curDepth = si[1] + 1
            if curDepth >= depth[amount]: continue

            for amt in children(si[0]):
                if amt > amount: continue
                if amt == amount:
                    height[si[0]] = 1
                    depth[amount] = curDepth
                    break
                if curDepth >= depth[amt]: continue
                depth[amt] = curDepth

                stack.append((si[0], -amt))  # update height
                if height[amt] == height_inf: 
                    stack.append((amt, curDepth))

        return depth[amount] if depth[amount] < depth_inf else -1



print(Solution().coinChange([1,4,5], 12))
print('Stop')



    

        
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

count_failed = 0
for i, data in enumerate(test_data, start=1):
    s = Solution()
    ans = s.coinChange(data['coins'], data['amt'])
    if ans == data['ans']:
        print(f'Test #{i} passed!!')
    else:
        count_failed += 1
        print(f'Test #{i} FAILED********')

if count_failed:
    print(f'{count_failed} test(s) FAILED')