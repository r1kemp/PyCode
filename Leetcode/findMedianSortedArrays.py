

class Solution:
    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B) or (len(A) == len(B) and A[-1] > B[-1]):
            A, B = B, A

        if len(A) == 0:
            m = (len(B) + 1) // 2
            if len(B) % 2 == 1: return B[m-1] / 1
            else:               return (B[m-1] + B[m]) / 2
        elif len(A) == 1 and len(B) == 1:
            return (A[0] + B[0]) / 2

        self.mid = (len(A) + len(B)) // 2

        import bisect
        b = bisect.bisect(B, A[-1])
        x, y = 0, 0
        if len(A) + b < self.mid:
            x = B[self.mid - len(A) - 1]
            y = B[self.mid - len(A)]
        else:
            x, y = self.findMids(A, 0, B, 0)
        
        oddLength = (len(A) + len(B)) % 2 == 1 
        return y / 1 if oddLength else (x + y) / 2

    def findMids(self, A, a, B, b):
        rem = self.mid - a - b
        if rem == 1:
            if a < len(A) and A[a] < B[b]: a += 1
            else: b += 1
            rem -= 1

        if rem == 0:
            x, y = 0, 0

            if a == 0:  x = B[b-1]
            elif b > 0: x = max(A[a-1], B[b-1])
            else:       x = A[a-1]

            if a == len(A): y = B[b]
            else:           y = min(A[a], B[b])
            
            return (x, y)

        rem //= 2
        an = a + rem
        bn = b + rem

        if an >= len(A):
            bn += an - len(A) + 1
            an = len(A) - 1

        assert an >= 0 and an < len(A)

        import bisect
        if an >= 0 and an < len(A) and A[an] < B[bn]:
            bn = bisect.bisect(B, A[an], b, bn+1)
        elif B[bn] < A[an]:
            an = bisect.bisect(A, B[bn], a, an+1)

        return self.findMids(A, an, B, bn)
        
def bfFindMedian(C, B):
    C.extend(B)
    C.sort()
    n = len(C)
    m = (n + 1) // 2
    if n % 2 == 1:
        return C[m-1] / 1
    else:
        return (C[m-1] + C[m]) / 2
        
        
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
    ans = s.findMedianSortedArrays(A[i], B[i])
    ansExpected = bfFindMedian(A[i], B[i])
    if ans == ansExpected:
        print(f'TEST {i + 1} passed!')
    else:
        print(f'TEST {i + 1} failed **********')
        print(f'   expected = {ansExpected},  got = {ans}')

from random import randint
def run_test(i):
    nA = randint(0, 100)
    nB = randint(1, 100)

    A = [randint(20, 1000) for _ in range(nA)]
    B = [randint(20, 1000) for _ in range(nB)]
    
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
        assert False and 'Stopping due to failed test'

for i in range(205):
    run_test(i)

# def simpleFindMedian(A, B):
#     isEven = lambda x: x % 2 == 0

#     if len(A) > len(B) or (len(A) == len(B) and A[-1] > B[-1]):
#         A, B = B, A

#     mid = (len(A) + len(B) + 1) // 2
#     a, b = 0, 0
#     for _ in range(mid-1):
#         if A[a] < B[b]: a += 1
#         else: b += 1

#     median = 0
#     if a < len(A) and A[a] < B[b]:
#         median = A[a]
#         a += 1
#     else:
#         median = B[b]
#         b += 1

#     if isEven(len(A) + len(B)):
#         median += A[a] if a < len(A) and A[a] < B[b] else B[b]
#         median /= 2
#     else:
#         median /= 1

#     return median

