
class pair(object):
    def __init__(self, h, val):
        self.h = h
        self.val = val
    def __lt__(self, other):
        return self.h < other.h
    def __gt__(self, other):
        return self.h > other.h
    def __le__(self, other):
        return self.h <= other.h
    def __ge__(self, other):
        return self.h >= other.h
    def __repr__(self):
        return str(self)
    def __str__(self):
        return '({0}, {1})'.format(self.h, self.val)

# p = pair(5, 15)
# q = pair(7, 77)
# print(p < q)

# from sortedcontainers import SortedList
# sln = SortedList()
# sln.add(pair(5, 15))
# sln.add(pair(25, 15))
# sln.add(pair(12, 15))
# sln.add(pair(2, 35))
# sln.add(pair(18, 15))
# print(sln)

def maxEnvelopes(envelopes):
    if len(envelopes) == 0:
        return 0

    # ev = sorted(envelopes, key=lambda x: x[0])
    # xevs = [[ev[0][1]]]
    # iCurr = 0
    # xCurr = ev[0][0]
    # for i in range(1, len(ev)):
    #     if ev[i][0] == xCurr:
    #         xevs[iCurr].append(ev[i][1])
    #     else:
    #         xevs[iCurr].sort() 
    #         iCurr += 1
    #         xCurr = ev[i][0]
    #         xevs.append([ev[i][1]])
    # xevs[iCurr].sort() 

    ev = sorted(envelopes, key=lambda x: x[0])
    xevs = [set([ev[0][1]])]
    iCurr = 0
    xCurr = ev[0][0]
    for i in range(len(ev)):
        if ev[i][0] == xCurr:
            xevs[iCurr].add(ev[i][1])
        else:
            xevs[iCurr] = list(xevs[iCurr])
            xevs[iCurr].sort() 
            iCurr += 1
            xCurr = ev[i][0]
            xevs.append(set([ev[i][1]]))
    xevs[iCurr] = list(xevs[iCurr])
    xevs[iCurr].sort() 


    # for x in xevs:
    #     print(x)

    from sortedcontainers import SortedList
    from bisect import bisect_left

    cumList = SortedList()

    for hList in xevs:
        if len(cumList) == 0:
            cumList.add(pair(min(hList), 1))
        else:
            tempList = []
            for h in hList:
                i = bisect_left(cumList, pair(h, 0))
                if i == 0:
                    if cumList[i].h != h:
                        tempList.append(pair(h, 1))
                elif i == len(cumList):
                    hVal = cumList[len(cumList)-1].val + 1
                    tempList.append(pair(h, hVal))
                elif cumList[i].h == h:
                    hVal = cumList[i-1].val + 1
                    if cumList[i].val < hVal:
                        cumList[i].val = hVal
                else:
                    hVal = cumList[i-1].val + 1
                    tempList.append(pair(h, hVal))
            cumList.update(tempList)
            for i in range(len(cumList)-1, 0, -1):
                if cumList[i].val == cumList[i-1].val:
                    del cumList[i]
                
    return max(p.val for p in cumList)
    
    


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

envelopes = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
envelopes.sort(key= lambda x: (x[0], -x[1]))
print(envelopes)