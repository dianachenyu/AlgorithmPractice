from functools import cache 
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        @cache
        def dp(mask, last):
            # base case: tricky, need to add the last element of cost
            if mask == (1 << n) - 1:
                return abs(last - nums[0]), []
            
            min_cost= float('inf')
            min_perm = None
            for cur in range(n):
                if mask & 1 << cur:
                    continue
                cost, perm = dp(mask | 1 << cur, cur)
                cost += abs(last - nums[cur])
                if cost < min_cost:
                    min_cost = cost
                    min_perm = [cur] + perm
            return min_cost, min_perm
                
        return [0] + dp(1, 0)[1]

# Bit mask + DP
# observation: the cost does not change if we rotate the array. only relative ordering matters. So we can set perm[0] = 0 for the smallest lexical order.
