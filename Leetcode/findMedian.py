class Solution:
    def findMedian(self, A, B):
        if len(A) > len(B):
            A, B = B, A

        cMedian = (len(A) + len(B) + 1) // 2
        if len(A) == 0: 
            x, y = B[cMedian - 1], B[cMedian]
        else:
            x, y = self.rFindMedian(A, 0, len(A)-1, B, 0, len(B)-1, cMedian)

        oddLen = len(B) % 2 == 1
        return x/1 if oddLen else (x+y)/2
    
    def rFindMedian(self, A, aMin, aMax, B, bMin, bMax, cMedian):
        aMid = (aMin + aMax) //  2
        while aMid < aMax and A[aMid] == A[aMid + 1]: aMid += 1

        from bisect import bisect
        b = bisect(B, A[aMid], bMin, bMax)
        
        if (b + aMid + 1) == cMedian:
             x = max(A[aMid], B[b])
             y = min(A[aMid + 1], B[b+1])
             return (x, y)       

        if (b + aMid + 1) < cMedian:
            aMin = aMid + 1
        else:
            aMax = aMin - 1

        return self.rFindMedian(A, aMin, aMax, B, bMin, bMax, cMedian)



        # combLen = len(A) + len(B)
        # mid = (combLen + 1) // 2
        # from bisect import bisect
        # aMin, aMax = 0, len(A)-1
        # while True:
        #     b = bisect(B, A[aMax])
        #     if (b + aMax + 1) < mid:
        #         m = mid - b - aMax - 1
        #         if combLen % 2 == 1:
        #             return B[b + m - 1]
        #         else:
        #             return (B[b + m - 1] + B[b + m]) // 2




# def findMedian(A, B):
#     if len(A) > len(B):
#         A, B = B, A

#     if len(A) == 0:
#         if len(B) % 2 == 0:
#             return (B[len(B) // 2 - 1] + B[len(B) // 2]) / 2
#         else:
#             return B[len(B) // 2] / 1

#     combLen = len(A) + len(B)
#     mid = (combLen + 1) // 2
#     from bisect import bisect
#     aMin, aMax = 0, len(A)-1
#     while True:
#         b = bisect(B, A[aMax])
#         if (b + aMax + 1) < mid:
#             m = mid - b - aMax - 1
#             if combLen % 2 == 1:
#                 return B[b + m - 1]
#             else:
#                 return (B[b + m - 1] + B[b + m]) // 2



