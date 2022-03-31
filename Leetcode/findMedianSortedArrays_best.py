
class Solution:
    def findMedianSortedArrays(self, A, B):
        # ensure list A is shorter than or equal to list B
        if len(A) > len(B): A, B = B, A

        # let i be the index in A
        # let j be the index in B
        # medianLen = (total items is A & B + 1) // 2
        
        # To find the median we need to find i and j such that 
        #   i + j == medianLen
        # and 
        #   List elements A[0], A[1], .., A[i-1] are less than or equal to B[j]
        #   List elements B[0], B[1], .., B[i-1] are less than or equal to A[i]
        # This can be done by ensuring
        #   A[i-1] <= B[j]  and B[j-1] <= A[i]
        #     a1   <= b2    and   b1   <= a2
        #
        # we will do a binary search on A (the shorter of the two lists) to 
        # find i. 

        medianLen = (len(A) + len(B) + 1) // 2
        minVal = min(A[0], B[0]) - 1 if len(A) else B[0] - 1
        maxVal = max(A[-1], B[-1]) + 1 if len(A) else B[-1] + 1
        oddLen = (len(A) + len(B)) % 2 == 1

        iLeft, iRight = 0, len(A)

        while iLeft <= iRight:
            iMid = (iLeft + iRight) // 2
            jMid = medianLen - iMid

            a1 = A[iMid - 1] if iMid else minVal
            a2 = A[iMid] if iMid < len(A) else maxVal
            b1 = B[jMid - 1] if jMid else minVal
            b2 = B[jMid] if jMid < len(B) else maxVal

            if a1 <= b2 and b1 <= a2:
                return max(a1, b1) / 1 if oddLen else (max(a1, b1) + min(a2, b2)) / 2
            elif a1 > b2:
                iRight = iMid - 1
            else:
                iLeft = iMid + 1


def bfFindMedian(A, B):
    A = A + B
    A.sort()
    n = len(A)
    m = (n + 1) // 2
    if n % 2 == 1: return A[m-1] / 1
    else:           return (A[m-1] + A[m]) / 2

s = Solution()
A = [1,3,5,7,9]
B = [2,4,6,8,10]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

A = [32, 62, 71, 98]
B = [31, 39, 60, 61, 62, 79, 80, 84]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

A = [70, 83]
B = [25, 35, 36, 57, 59, 61, 70, 72, 81, 83, 98]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

A = [102, 109, 132, 146, 183, 200, 225, 267]
B = [25, 35, 36, 57, 59, 61, 70, 72, 81, 83, 98]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

A = [83]
B = [54, 78]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

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
    ans = s.findMedianSortedArrays(A[i], B[i])
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
    ans = s.findMedianSortedArrays(A, B)
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