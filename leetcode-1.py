# leetcode-1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def intToListNode(self, num):
#         if num == 0: 
#             return ListNode()

#         head = ListNode(num % 10)
#         num //= 10
#         curr = head
#         while num > 0:
#             curr.next = ListNode(num % 10)
#             curr = curr.next
#             num //= 10
#         return head
        
#     def listNodeToInt(self, l1):
#         result = 0
#         multiplier = 1
#         while l1 != None:
#             result += l1.val * multiplier
#             multiplier *= 10
#             l1 = l1.next
#         return result
        
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         a = self.listNodeToInt(l1)
#         b = self.listNodeToInt(l2)
#         c = a + b
#         return self.intToListNode(c)
    
# sln = Solution()
# l1 = sln.intToListNode(342)
# l2 = sln.intToListNode(465)
# l3 = sln.addTwoNumbers(l1, l2)
# print(sln.listNodeToInt(l3))


# def isValid_v1(s):                
#     stack = []
#     for ch in s:
#         if ch in '([{':
#             stack.append(ch)
#         else:
#             if len(stack) == 0:
#                 return False
#             last = stack.pop()
#             if ch == ')' and last != '(':
#                 return False
#             if ch == ']' and last != '[':
#                  return False
#             if ch == '}' and last != '{':
#                 return False
#     return len(stack) == 0

# def isValid(s):                
#     stack = []
#     map = {')':'(', '}':'{', ']':'['}

#     for ch in s:
#         if ch in map:
#             if not stack: # len(stack) == 0:
#                 return False

#             top_element = stack.pop()
#             if map[ch] != top_element:
#                 return False
#         else:
#             stack.append(ch)

#     return not stack




# def testPara(s, exp, id):
#     res = isValid(s)
#     if res == exp:
#         print('test', id, 'passed!')
#     else:
#         print('test', id, 'failed *****')

# testPara('()', True, 1)
# testPara('()[]{}', True, 2)
# testPara('([{}])', True, 3)
# testPara('()[{}]', True, 4)
# testPara('', True, 5)
# testPara('(]', False, 6)
# testPara(']', False, 7)
# testPara('()]', False, 8)
# testPara('({}]', False, 9)

# def lengthOfLIS(nums):
#     if len(nums) == 0:
#         return 0

#     import bisect
#     dp = [nums[0]]
#     for n in range(1, len(nums)):
#         i = bisect.bisect_left(dp, nums[n])
#         if i < len(dp):
#             dp[i] = nums[n]
#         else:
#             dp.append(nums[n])
#     return len(dp)

# def lengthOfLIS(nums):
#         import bisect
#         dp = []
#         for n in range(len(nums)):
#             i = bisect.bisect_left(dp, nums[n])
#             if i < len(dp):
#                 dp[i] = nums[n]
#             else:
#                 dp.append(nums[n])
#         return len(dp)


# print(lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(lengthOfLIS([]))
# print(lengthOfLIS([10,9,2]))

# def largestDivisibleSubset(nums):
#     if len(nums) == 0:
#         return []

#     nums = sorted(nums)
#     dp = [0] * len(nums)
#     prev = [-1] * len(nums)
#     iMax = 0
#     for i in range(len(nums)):
#         count = 0
#         for j in range(i-1, -1, -1):
#             if nums[i] % nums[j] == 0:
#                 if dp[j] > count:
#                     count = dp[j]
#                     prev[i] = j
#         dp[i] = count + 1
#         if dp[i] > dp[iMax]:
#             iMax = i

#     res = []
#     while iMax != -1:
#         res.append(nums[iMax])
#         iMax = prev[iMax]

#     return sorted(res)
        
    

# print(largestDivisibleSubset([1,2,42,3,4,6,7,9,27]))
# print(largestDivisibleSubset([4,8,10,240]))

# def maxEnvelopes(envelopes):
#     if len(envelopes) == 0:
#         return 0

#     ev = sorted(envelopes, key=lambda x: -x[1])
#     ev = sorted(ev, key=lambda x: x[0])

#     count = [1] * len(ev)
#     for i in range(len(ev) - 2, -1, -1):
#         for j in range(i+1, len(ev)):
#             if ev[i][0] < ev[j][0] and ev[i][1] < ev[j][1]:
#                 tempCount = count[j] + 1
#                 if count[i] < tempCount:
#                     count[i] = tempCount
#     return max(count)

# from sortedcontainers import SortedList
# from bisect import bisect_left

# def maxEnvelopes(envelopes):
#     if len(envelopes) == 0:
#         return 0

#     ev = sorted(envelopes, key=lambda x: x[0])
#     # xevs = [[[ev[0][1], 1]]]
#     xevs = [[ev[0][1]]]
#     iCurr = 0
#     xCurr = ev[0][0]
#     for i in range(1, len(ev)):
#         if ev[i][0] == xCurr:
#             xevs[iCurr].append(ev[i][1])
#         else:
#             xevs[iCurr].sort() #key=lambda x: x[0])
#             iCurr += 1
#             xCurr = ev[i][0]
#             xevs.append([ev[i][1]])
#     xevs[iCurr].sort() #key=lambda x: x[0])
#     # for x in xevs:
#     #     print(x)

#     maxVal = 1

#     hList = SortedList()
#     for wList in xevs:
#         if len(hList) == 0:
#             for el in wList:
#                 hList.add([el, 1])
#         else:
#             hListCurr = []
#             for el in wList:
#                 i = bisect_left(hList, [el, 0])
#                 if i == len(hList):
#                     elVal = 1 + hList[i-1][1]
#                     hListCurr.append([el, elVal])
#                     if elVal > maxVal:
#                         maxVal = elVal
#                     continue
#                 if hList[i][0] == el:
#                     if i > 0 and hList[i-1][1] + 1 > hList[i][1]:
#                         hList[i][1] = hList[i-1][1] + 1
#                         if hList[i][1] > maxVal:
#                             maxVal = hList[i][1]
#                     continue
#                 if hList[i][0] > el:
#                     i -= 1
#                 if i >= 0:
#                     elVal = 1 + hList[i][1]
#                     hListCurr.append([el, elVal])
#                     if elVal > maxVal:
#                         maxVal = elVal
#                 else:
#                     hListCurr.append([el, 1])
#             hList.update(hListCurr)
#     return maxVal

        


# print(maxEnvelopes([]))    
# print(maxEnvelopes([[3, 4], [12, 15], [12, 5], [12, 2], [30, 6]]))
# print(maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))
# print(maxEnvelopes([[2,10],[3,20],[4,30],[5,50],[5,40],[5,25],[6,37],[6,36],[7,38]]))
# print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))

import collections

class Solution(object):
    def isAnagram(self, s1, p):
        return collections.Counter(s1) == self.pCounter

    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        self.pCounter = collections.Counter(p)

        val = lambda x: ord(x) - ord('a') + 1

        defChars = [1]*27
        for c in p:
            defChars[val(c)] = 0

        defCount = 0
        for i in range(len(p)):
            defCount += defChars[val(s[i])]

        result = []

        for i in range(len(s) - len(p) + 1):
            j = i + len(p) - 1
            if defCount == 0:
                if self.isAnagram(s[i:j+1], p):
                    result.append(i)
            
            if j < len(s) - 1:
                defCount = defCount - defChars[val(s[i])] + defChars[val(s[j+1])]
        
        return result

sln = Solution()
print(sln.findAnagrams("cbaebabacd", "abc"))
print(sln.findAnagrams("cba", "z"))

sIn = "afdkljflsdkjfsdlkjfdslkjfdslkjfkljlkjlkfdjslkfjsdlkjsdflksdjflkdsjfldskjksldfjlksdjflkdsjfsjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjfsdfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
pIn = "z"
# print(sln.findAnagrams(sIn, pIn))


# class Solution(object):
#     def isAnagram(self, s1, p):
#         return collections.Counter(s1) == self.pCounter

#     def findAnagrams(self, s, p):
#         if len(s) < len(p):
#             return []
            
#         self.pCounter = collections.Counter(p)

#         val = lambda x: ord(x) - ord('a') + 1

#         defChars = [1]*27
#         pVal = 0
#         for c in p:
#             cVal = val(c)
#             defChars[cVal] = 0
#             pVal += cVal

#         defCount = 0
#         currVal = 0
#         for i in range(len(p)):
#             c = s[i]
#             cVal = val(c)
#             defCount += defChars[cVal]
#             currVal += cVal

#         result = []

#         for i in range(len(s) - len(p) + 1):
#             j = i + len(p) - 1
#             if defCount == 0 and currVal == pVal:
#                 if self.isAnagram(s[i:j+1], p):
#                     result.append(i)
            
#             if j < len(s) - 1:
#                 defCount = defCount - defChars[val(s[i])] + defChars[val(s[j+1])]
#                 currVal = currVal - val(s[i]) + val(s[j+1])
        
#         return result
