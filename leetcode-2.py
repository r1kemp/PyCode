# leetcode-2.py


# def maxEnvelopes(envelopes):
#     if len(envelopes) == 0:
#         return 0
#     ev = sorted(envelopes, key=lambda x: (x[0], -x[1]))
#     hts = [x[1] for x in ev]
#     # print(hts)
#     uhts = [hts[0]]
#     for i in range(1, len(hts)):
#         if hts[i] != hts[i-1]:
#             uhts.append(hts[i])
#     # print(uhts)

#     import bisect
#     run = []
#     for h in uhts:
#         i = bisect.bisect_left(run, (h, 0))
#         count = 1
#         if i > 0:
#             count = run[i-1][1] + 1
        
#         if i < len(run):
#             run[i] = (h, count)
#         else:
#             run.append((h, count))

#     return run[len(run)-1][1]
    
def maxEnvelopes(envelopes):
    if len(envelopes) == 0:
        return 0
    ev = sorted(envelopes, key=lambda x: (x[0], -x[1]))

    hts = [x[1] for x in ev]
    uhts = [hts[0]]
    for i in range(1, len(hts)):
        if hts[i] != hts[i-1]:
            uhts.append(hts[i])

    import bisect
    run = []
    for h in uhts:
        i = bisect.bisect_left(run, h)
        
        if i < len(run):
            run[i] = h
        else:
            run.append(h)

    return len(run)


def testEnv(evs, ans):
    res = maxEnvelopes(evs)
    if res == ans:
        print('Passed!!')
    else:
        print('Test FAILED: \n maxEnvelopes({0}) returned {1}'.format(evs, res))

testEnv([], 0)

testEnv([[5,4],[6,4],[6,7],[2,3]], 3)

testEnv([[3, 4], [12, 15], [12, 5], [12, 2], [30, 6]], 3)

testEnv([[46,89],[50,53],[52,68],[72,45],[77,81]], 3)

testEnv([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
, 5)

testEnv([[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
, 5)