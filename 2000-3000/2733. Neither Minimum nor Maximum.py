class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        min_num = min(nums)
        max_num = max(nums)
        for num in nums:
            if num != min_num and num != max_num:
                return num
        return -1
