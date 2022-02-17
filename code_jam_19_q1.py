T = int(input())
for t in range(1, T+1):
    N = input()
    A = []
    B = []
    for n in N:
        if n == '4':
            A.append('3')
            B.append('1')
        else:
            A.append(n)
            if len(B) != 0:
                B.append('0')
    a = ''.join(A)
    b = ''.join(B)
    print('Case #' + str(t) + ':', a, b)
   