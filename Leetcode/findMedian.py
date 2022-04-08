class Solution:
    def findMedian(self, A, B):
        if len(A) > len(B): A, B = B, A

        combLen = len(A) + len(B)
        if combLen == 1: return B[0] / 1

        cMedian = (combLen + 1) // 2
        if cMedian <= 6:
            x, y = self.findElementsMandMp1(A, 0, B, 0, cMedian)
        elif len(A) == 0: 
            x, y = B[cMedian - 1], B[cMedian]
        else:
            x, y = self.rFindMedian(A, 0, len(A)-1, B, 0, len(B)-1, cMedian)

        oddLen = combLen % 2 == 1
        return x/1 if oddLen else (x+y)/2
    
    def rFindMedian(self, A, aMin, aMax, B, bMin, bMax, cMedian):
        aMid = (aMin + aMax) //  2
        while aMid < aMax and A[aMid] == A[aMid + 1]: aMid += 1

        from bisect import bisect
        b = bisect(B, A[aMid], bMin, bMax)
        
        if (b + aMid + 1) == cMedian:
            return self.findElementsMandMp1(A, aMid, B, b, cMedian)

        if (b + aMid + 1) < cMedian:
            if aMin < aMax:
                aMin = aMid + 1
            else:
                return self.findElementsMandMp1(A, aMin, B, b, cMedian)
        else:
            if aMid == aMin:
                return self.findElementsMandMp1(A, aMin, B, cMedian - aMin - 1, cMedian)
            if aMid > 0:
                aMax = aMid - 1
            else:
                aMax = 0

            if aMin > aMax: aMin = aMax

        return self.rFindMedian(A, aMin, aMax, B, bMin, bMax, cMedian)

    def findElementsMandMp1(self, A, a, B, b, M):
        m = a + b
        x, y = 0, 0
        while m < M:
            if a < len(A) and A[a] <= B[b]:
                x = A[a]
                a += 1
            else:
                x = B[b]
                b += 1
            m += 1

        if a == len(A):     y = B[b]
        elif b == len(B):   y = A[a]
        else:               y = A[a] if A[a] < B[b] else B[b]

        return (x, y)

def bfFindMedian(A, B):
    A = A + B
    A.sort()
    n = len(A)
    m = (n + 1) // 2
    if n % 2 == 1:
        return A[m-1] / 1
    else:
        return (A[m-1] + A[m]) / 2

s = Solution()
# A = [1,3,5,7,9]
# B = [2,4,6,8,10]

# A = [70, 83]
# B = [25, 35, 36, 57, 59, 61, 70, 72, 81, 83, 98]

# A = [102, 109, 132, 146, 183, 200, 225, 267]
# B = [25, 35, 36, 57, 59, 61, 70, 72, 81, 83, 98]

# A = [32, 62, 71, 98]
# B = [31, 39, 60, 61, 62, 79, 80, 84]
A = [83]
B = [54, 78]

ans = s.findMedian(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

s = Solution()
A, B = [], []
A.append([1])                       # test 1
B.append([1])
A.append([1,3,5,7,999])                     # test 2
B.append( [2,4,6,8,9,10,11,12,13,14,15])
A.append([1,2,3,4,55,56,57,58,59])          # test 3
B.append([6,7,8,9,10])
A.append([1,2,3,4,5])                       # test 4
B.append([])
for i in range(len(A)):
    ansExpected = bfFindMedian(A[i], B[i])
    ans = s.findMedian(A[i], B[i])
    if ans == ansExpected:
        print(f'TEST {i + 1} passed!')
    else:
        print(f'TEST {i + 1} failed **********')
        print(f'   expected = {ansExpected},  got = {ans}')

f = open('data.txt', 'a')
from random import randint
def run_test(i):
    nA = randint(1, 115)
    nB = randint(1, 115)

    A = [randint(20, 99999) for _ in range(nA)]
    B = [randint(20, 99999) for _ in range(nB)]
    
    A.sort()
    B.sort()

    s = Solution()
    ans = s.findMedian(A, B)
    ansExpected = bfFindMedian(A, B)
    if ans == ansExpected:
        print(f'TEST {i + 1} passed!')
    else:
        print(f'TEST {i + 1} failed **********')
        print(f'   expected = {ansExpected},  got = {ans}')
        f.write(f'A = {A}\n')
        f.write(f'B = {B}\n')
        f.close()
        assert False and 'Stopping due to failed test'

for i in range(205):
    run_test(i)

f.close()