# maximizeModulo


K, M = map(int, input().split())
main_set = set()
for _ in range(K):
    S = list(map(int, input().split()))
    T = {e % M for e in S[1:]}
    N = {((e*e) % M) for e in T}

    if len(main_set) == 0:
        main_set = N    
    else:
        temp_set = set()
        for e1 in main_set:
            for e2 in N:
                temp_set.add((e1 + e2 ) % M)

        main_set = temp_set

print(max(main_set))



