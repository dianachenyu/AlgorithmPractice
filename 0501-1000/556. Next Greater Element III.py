# Time O(m), m = number of digits in the integer, m <= 10 in this question. so O(1)
# Space O(m) 

class Solution:
    def nextGreaterElement(self, num: int) -> int:
        res = list(str(num))
        n = len(res)
        i = n - 1
        while i > 0:
            if res[i] <= res[i - 1]:
                i -= 1
            else:
                min_digit = min(digit for digit in res[i:] if digit > res[i-1])
                j = max(idx + i for idx, digit in enumerate(res[i:]) if digit == min_digit)
                res[i - 1], res[j] = res[j], res[i - 1]
                res[i:] = res[i:][::-1]
                ans = int(''.join(res))
                return -1 if ans > 2 ** 31 - 1 else ans 
        return -1
      
