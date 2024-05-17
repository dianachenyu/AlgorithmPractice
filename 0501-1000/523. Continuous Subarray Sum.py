class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        presum = 0
        for idx, num in enumerate(nums):
            presum = (presum + num) % k
            if presum in d and d[presum] <= idx - 2:
                return True
            if not presum in d:
                d[presum] = idx
        return False 


        
