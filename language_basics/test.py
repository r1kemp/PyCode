# test

class Solution:
    def isAlphaNumeric1(self, c: str) -> bool:
        return (c[0] >= 'a' and c[0] <= 'z') or (c[0] >= 'A' and c[0] <= 'Z')  or (c[0] >= '0' and c[0] <= '9')
    
    def isAlphaNumeric(self, c: str) -> bool:
        atoz = 'abcdefghijklmnopqrstuvwxyz'
        AN = atoz + atoz.upper() + '0123456789'
        return c in AN
    
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1

            while right > left and not self.isAlphaNumeric(s[right]):
                right -= 1
             
            if left >= right:
                break
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

sln = Solution()
assert(sln.isPalindrome('=A?'))
assert(sln.isPalindrome('=?'))
assert(sln.isPalindrome(" "))
assert(not sln.isPalindrome('race a car'))
assert(sln.isPalindrome("A man, a plan, a canal: Panama"))
print('All tests passed')

def mergeTwoLists(A, B):
      C = list()
      a = 0
      b = 0
      while a < len(A) and b < len(B):
            if A[a] < B[b]:
                  C.append(A[a])
                  a += 1
            else:
                  C.append(B[b])
                  b += 1
      
      assert (a == len(A) or b == len(B))

      while a < len(A):
            C.append(A[a])
            a += 1

      while b < len(B):
            C.append(B[b])
            b += 1

      return C

c = mergeTwoLists([1,2,4], [1,3,4])
print(c)
c = mergeTwoLists([], [])
print(c)
