class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and math.gcd(num, stack[-1]) > 1:
                lnum = stack.pop()
                num = lnum * num // math.gcd(num, lnum)
            stack.append(num)
        return stack

      
# Time O(NlogM) N = len(nums), M = max(nums)
# Space O(N)
