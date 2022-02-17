#
#  https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
#
#  https://github.com/kamyu104/GoogleKickStart-2020
#

T = int(input())
for t in range(1, T+1):
    N, K, P = (int(x) for x in input().split(' '))
    S = []
    for _ in range(N):
        s_i = [int(x) for x in input().split(' ')]
        if P < K:
            s_i = s_i[:P]

        s_i = [0] + s_i

        for i in range(1, len(s_i)):
            s_i[i] += s_i[i-1]
        S.append(s_i)
        
    dp = [0] * (P + 1)
    if P < K:
        K = P
    for i in range(K + 1):
        dp[i] = S[0][i]

    dp2 = [0] * (P+ 1)

    for i in range(1, N):
        for p in range(P+1):
            dp2[p] = 0
            left, right = p, 0
            while left >= 0 and right <= K:
                val = dp[left] + S[i][right]
                dp2[p] = max(dp2[p], val)
                left -= 1
                right += 1

        dp, dp2 = dp2, dp

    print(f'Case #{t}: {dp[P]}')


    # for i in range(1, N):
    #     for p in range(1, P+1):
    #         if p <= K:
    #             left, right = p, 0
    #             while left >= 0:
    #                 val = dp[left] + S[i][right]
    #                 dp2[p] = max(dp2[p], val)
    #                 left -= 1
    #                 right += 1
    #         else:
    #             left, right = K, p - K
    #             while right <= K:
    #                 val = dp[left] + S[i][right]
    #                 dp2[p] = max(dp2[p], val)
    #                 left -= 1
    #                 right += 1
    #     dp, dp2 = dp2, dp