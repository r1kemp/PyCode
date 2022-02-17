# Play

T = int(input())
for t in range(1, T+1):
    N, K, P = (int(x) for x in input().split(' '))
    S = []
    for _ in range(N):
        s_i = [int(x) for x in input().split(' ')]
        s_i = [0] + s_i[:P]

        for i in range(1, len(s_i)):
            s_i[i] += s_i[i-1]

        S.append(s_i)

    if P < K: K = P

    if N == 1:
        print(f'Case #{t}: {S[0][P]}')

    if N == 2:
        maxVal = 0
        for i in range(K+1):
            for j in range(K+1):
                if i + j != P:
                    continue
                maxVal = max(maxVal, S[0][i] + S[1][j]) 

        print(f'Case #{t}: {maxVal}')

    if N == 3:
        maxVal = 0
        for i in range(K+1):
            for j in range(K+1):
                for k in range(K+1):
                    if i + j + k != P:
                        continue
                    maxVal = max(maxVal, S[0][i] + S[1][j] + S[2][k])

        print(f'Case #{t}: {maxVal}')

    if N == 4:
        maxVal = 0
        for i in range(K+1):
            for j in range(K+1):
                for k in range(K+1):
                    for l in range(K+1):
                        if i + j + k + l != P:
                            continue
                        currVal = S[0][i] + S[1][j] + S[2][k] + S[3][l] 
                        print(f'{S[0][i]} + {S[1][j]} + {S[2][k]} + {S[3][l]} = {currVal}')
                        maxVal = max(maxVal, S[0][i] + S[1][j] + S[2][k] + S[3][l])

        print(f'Case #{t}: {maxVal}')
