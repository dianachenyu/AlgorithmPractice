class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for num in nums[1:]:
            res &= set(num)
        return sorted(res)
        
        
