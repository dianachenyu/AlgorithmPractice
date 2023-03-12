class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        res = 0
        prefix = 0
        counter = collections.Counter({0: 1})
        
        for num in nums:
            prefix ^= num
            res += counter[prefix]
            counter[prefix] += 1
        return res
               
        
# Bit Operation
