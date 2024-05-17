class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        counter = collections.Counter([presum])
        res = 0

        for num in nums:
            presum += num
            res += counter[presum-k]
            counter[presum] += 1
        return res
