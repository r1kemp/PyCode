
import typing

''' 
Use a list to store the new nodes visited at each depth.

Example: coins = [1, 3, 5], amount = 11

At step 0:  A = [0] 
At step 1:  A = [1, 3, 5]
At step 2:  A = [2, 4, 6, 8, 10]
At step 3:  A = [7, 9, 11]  <-- stops as soon as we hit 11 (the desired amount)

'''
def coinChange(coins: typing.List[int], amount: int) -> int:
    if not amount: return 0
    A = [0]
    B = []
    visited = [False]*(amount + 1)
    depth = 0
    coins.sort()
    while A and depth < amount:
        depth += 1
        for coin in coins:
            for a in A:
                anext = a + coin
                if anext > amount: continue
                if anext == amount: return depth
                if not visited[anext]: 
                    B.append(anext)
                    visited[anext] = True

        A, B = B, A
        B.clear()

    return -1

def coinChange_pythonic(coins: typing.List[int], amount: int) -> int:
    A, visited, depth = {0}, {0}, 0
    while A and amount not in A:
        if amount in A: return depth
        A = {a + coin for a in A for coin in coins if a + coin <= amount and a + coin not in visited}
        visited.update(A)
        depth += 1
    
    return depth if amount in A else -1




# slight modification to the function above
# (minor speed improvement)
def coinChange_sort_coins(coins: typing.List[int], amount: int) -> int:
    if not amount: return 0
    A = [0]
    B = []
    visited = [False]*(amount + 1)
    depth = 0
    coins.sort()
    while A and depth < amount:
        depth += 1
        for coin in coins:
            for a in A:
                anext = a + coin
                if anext > amount: 
                    break   # changeed continue to break (reduces cost)
                if anext == amount: return depth
                if not visited[anext]: 
                    B.append(anext)
                    visited[anext] = True

        A, B = B, A
        B.clear()
        A.sort()    # added this sorting (increases cost)

    return -1


test_data = [
    {'coins':[3,5], 'amt': 2, 'ans': -1},
    {'coins':[1,2,5], 'amt': 4, 'ans': 2},
    {'coins':[1], 'amt': 0, 'ans': 0},
    {'coins':[3,5], 'amt': 0, 'ans': 0},
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
    ans = coinChange_pythonic(data['coins'], data['amt'])
    if ans == data['ans']:
        print(f'Test #{i} passed!!')
    else:
        count_failed += 1
        print(f'Test #{i} FAILED********')

if count_failed:
    print(f'{count_failed} test(s) FAILED')