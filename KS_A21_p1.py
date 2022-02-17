T = int(input())
for t in range(1, T+1):
    N, K = (int(x) for x in input().split(' '))
    s = input()
    l, r = 0, N-1
    g = 0
    while l < r:
        if s[l] != s[r]:
            g += 1
        l, r = l + 1, r - 1
    print('Case #{}: {}'.format(t, abs(K - g)))
