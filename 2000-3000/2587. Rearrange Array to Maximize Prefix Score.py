class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            res += prefix > 0
        return res 

