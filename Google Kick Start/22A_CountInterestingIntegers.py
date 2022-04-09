'''
This is the solution given by them. (Not my work)
'''

from functools import cache

f = open("c:\\temp\\out.txt", 'w')

def CountDigits(N):
    return len(str(N))

def GetIthDigit(N, digit_index):
    return int(str(N)[digit_index])

# @cache
def f1(L, P, S):
    f.write(f'f1({L}, {P}, {S})\n')
    if L == 0:
        return 1 if P%S == 0 else 0
    ans = 0
    for d in range(10):
        ans += f1(L - 1, P * d, S + d)
    return ans

def CountInterestingIntegers(N):
  if N == 0:
    return 0
  count = 0
  for L in range(1, CountDigits(N)):
    count += CountInterestingIntegersWithNumberOfDigits(L)

  count += CountInterestingIntegersWithPrefixOfN(N, P=1, S=0, digit_index=0, is_first_digit=True)
  return count

def CountInterestingIntegersWithNumberOfDigits(L):
  count = 0
  for digit in range(1, 10):
    count += f1(L - 1, P=digit, S=digit)
  return count

def CountInterestingIntegersWithPrefixOfN(N, P, S, digit_index, is_first_digit):
  if digit_index == CountDigits(N):
    return 1 if S > 0 and P % S == 0 else 0

  if is_first_digit:
    digit_start = 1
  else:
    digit_start = 0

  count = 0
  for digit in range(digit_start, GetIthDigit(N, digit_index)):
    count += f1(CountDigits(N) - digit_index - 1, P * digit, S + digit)

  count += CountInterestingIntegersWithPrefixOfN(N,
                                                 P * GetIthDigit(N, digit_index),
                                                 S + GetIthDigit(N, digit_index),
                                                 digit_index + 1, is_first_digit=False)
  return count

# a18 = CountInterestingIntegers(1000000000000)
a18 = CountInterestingIntegers(22)
print(a18)
f.close()