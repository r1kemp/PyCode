
class Solution:
    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B): A, B = B, A

        lenA, lenB = len(A), len(B)
        midElemNum = (lenA + lenB + 1) // 2
        oddlen = (len(A) + len(B)) % 2 == 1

        a, b = 0, 0
        required = midElemNum - 2
        while required > 0:
            if a == lenA:
                if oddlen:
                    return B[midElemNum - lenA - 1] / 1.0
                else:
                    return (B[midElemNum - lenA - 1] + B[midElemNum - lenA]) / 2.0

            delta = (required + 1) // 2

            aTemp = (a + delta) if (a + delta) <= lenA else lenA
            if A[aTemp - 1] <= B[b + delta - 1]: a, delta = aTemp, aTemp - a
            else:            b += delta

            required -= delta

        for _ in range(min(2, midElemNum)):
            if a < lenA and A[a] <= B[b]: a += 1
            else: b += 1

        minVal = min(A[0], B[0]) - 1
        maxVal = max(A[-1], B[-1]) + 1

        a1 = A[a-1] if a else float('-inf')
        b1 = B[b-1] if b else float('-inf')
        a2 = A[a] if a < lenA else float('inf')
        b2 = B[b] if b < lenB else float('inf')
        if oddlen:
            return max(a1, b1) / 1.0
        else:
            return (max(a1, b1) + min(a2, b2)) / 2.0

        
def bfFindMedian(A, B):
    A = A + B
    A.sort()
    n = len(A)
    m = (n + 1) // 2
    if n % 2 == 1: return A[m-1] / 1
    else:           return (A[m-1] + A[m]) / 2

s = Solution()
A = [0,0,0,0,0]
B = [-1,0,0,0,0,0,1]
# A = [5]
# B = [1,2,3,4,6,7,8,9,10,11,12,13,14,15]
ansE = bfFindMedian(A, B)
ans = s.findMedianSortedArrays(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

A = [1,2,3,4,5,6,17]
B = [x for x in range(7,17)]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

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

A = [83]
B = [54, 78]
ans = s.findMedianSortedArrays(A, B)
ansE = bfFindMedian(A, B)
print(f'{ans}, {ansE}, {ans == ansE}')

A = [102, 109, 132, 146, 183, 200, 225, 267]
B = [25, 35, 36, 57, 59, 61, 70, 72, 81, 83, 98]
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