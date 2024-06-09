class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = collections.Counter([0])
        presum = 0
        res = 0
        for num in nums:
            presum = (presum + num) % k
            res += count[presum]
            count[presum] += 1
        return res

  
