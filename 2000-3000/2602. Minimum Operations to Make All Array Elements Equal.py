class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        presum = [0] + list(itertools.accumulate(nums))
        n = len(nums)
        m = len(queries)
        res = [0] * m
        
        for idx, query in enumerate(queries):
            pivot = bisect.bisect_left(nums, query)
            res[idx] = pivot * query - presum[pivot] + (presum[-1] - presum[pivot]) - (n - pivot) * query
        return res 
        

# Prefix Sum 
# Time O((N + M) * log(N))
# Space O(N + M)
        
