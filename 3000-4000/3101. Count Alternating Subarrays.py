class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = 0
        for idx, num in enumerate(nums):
            if idx == 0 or num == nums[idx-1]:
                last_count = 1
            else:
                last_count += 1
            res += last_count
        return res 
