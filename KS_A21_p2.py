T = int(input())
for t in range(1, T+1):
    R, C = (int(x) for x in input().split(' '))
    maze = []
    E, W, N, S = [], [], [], []
    for r in range(R):
        l = [int(x) for x in input().split(' ')]
        maze.append(l)
        l = [0] * C
        E.append(l)
        l = [0] * C
        W.append(l)
        l = [0] * C
        N.append(l)
        l = [0] * C
        S.append(l)

    # print(maze)
    for r in range(R):
        for c in range(C):
