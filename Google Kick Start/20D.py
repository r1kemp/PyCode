'''
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08
Round D 2020 - Kick Start 2020
'''

# Problem #1: Record Breaker
def RecordBreaker():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        v = [int(x) for x in input().strip().split(' ')]
        if N == 1:
            print(f'Case #{t}: 1')
            continue

        ans = 1 if v[0] > v[1] else 0
        max_so_far = v[0]

        for i in range(1, N-1):
            if v[i] > max_so_far and v[i] > v[i+1]:
                ans += 1
            max_so_far = max(max_so_far, v[i])

        if v[N-1] > max_so_far:
            ans += 1
    
        print(f'Case #{t}: {ans}')    

# Problem #2: Alien Piano    
def AlienPiano():
    T = int(input())
    for t in range(1, T+1):
        K = int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ans = 0

        aKeysUsed = 1
        INC, DEC = 1, 2
        dirn = None

        for i in range(1, K):
            if A[i] == A[i-1]: continue
            elif A[i] < A[i-1]:
                if dirn == INC: 
                    aKeysUsed = 2
                    dirn = DEC
                elif dirn == DEC:
                    if aKeysUsed == 4:
                        ans += 1
                        aKeysUsed = 1
                    else:
                        aKeysUsed += 1
                else:
                    dirn = DEC
                    aKeysUsed = 2
            else: # a[i] > A[i-1]
                if dirn == DEC:
                    aKeysUsed = 2
                    dirn = INC
                elif dirn == INC:
                    if aKeysUsed == 4:
                        ans += 1
                        aKeysUsed = 1
                    else:
                        aKeysUsed += 1
                else:
                    dirn = INC
                    aKeysUsed = 2

        print(f'Case #{t}: {ans}')  


# Problem #3: Beauty of Tree
def BeautyOfTree_recursion():
    T = int(input())
    path = []
    for t in range(1, T+1):
        def dfs(node):
            path.append(node)
            for child in tree[node]:
                dfs(child)
            
            paintedByA[node] += 1
            paintedByB[node] += 1
            path.pop()
            if len(path) >= A: 
                paintedByA[path[-A]] += paintedByA[node]
            if len(path) >= B:
                paintedByB[path[-B]] += paintedByB[node]


        N, A, B = (int(x) for x in input().split(' '))
        print(f'*********  Case #{t}: N, A, B = {N}, {A}, {B}')
        line = input()
        if len(line) == 0:
            print(f'Case #{t}: 1.00000000')
            continue

        parent = [0, 0] + [int(x) for x in line.split(' ')]

        tree = [list() for _ in range(N+1)]
        for c in range(2, N+1):
            tree[parent[c]].append(c)

        paintedByA = [0] * (N+1)
        paintedByB = [0] * (N+1)

        dfs(1)
        nSquared = N * N
        numerator = 0
        for i in range(1, N+1):
            numerator += nSquared - (N - paintedByA[i]) * (N - paintedByB[i])
        
        ans = numerator / nSquared
        print(f'Case #{t}: {ans}')

def BeautyOfTree():
    T = int(input())
    path = []
    for t in range(1, T+1):
        def dfs():
            stack = [1]
            state = [0] * (N+1)

            while len(stack) > 0:
                node = stack[-1]
                if state[node] == 0:
                    for child in tree[node]:
                        stack.append(child)
                    path.append(node)
                    state[node] = 1
                else:
                    stack.pop()
                    path.pop()
            
                    paintedByA[node] += 1
                    paintedByB[node] += 1
                    if len(path) >= A: 
                        paintedByA[path[-A]] += paintedByA[node]
                    if len(path) >= B:
                        paintedByB[path[-B]] += paintedByB[node]


        N, A, B = (int(x) for x in input().split(' '))
        line = input()
        if len(line) == 0:
            print(f'Case #{t}: 1.00000000')
            continue

        parent = [0, 0] + [int(x) for x in line.split(' ')]

        tree = [list() for _ in range(N+1)]
        for c in range(2, N+1):
            tree[parent[c]].append(c)

        paintedByA = [0] * (N+1)
        paintedByB = [0] * (N+1)

        dfs()
        
        nSquared = N * N
        numerator = 0
        for i in range(1, N+1):
            numerator += nSquared - (N - paintedByA[i]) * (N - paintedByB[i])
        
        ans = numerator / nSquared
        print(f'Case #{t}: {ans}')

