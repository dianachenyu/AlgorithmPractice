class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = -1, -2
        max_left = nums[0]
        min_right = nums[-1]
        for i in range(1, len(nums)):
            if nums[i] < max_left:
                end = i
            max_left = max(max_left, nums[i])
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > min_right:
                start = i
            min_right = min(min_right, nums[i])
        return end - start + 1
 
