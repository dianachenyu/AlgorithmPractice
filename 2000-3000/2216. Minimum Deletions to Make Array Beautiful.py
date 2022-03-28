class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        leven = -1
        res = 0
        for num in nums:
            if leven < 0:
                leven = num
            elif num != leven:
                leven = -1
            else:
                res += 1
        if (len(nums) - res) %2 == 1:
            res += 1
        return res 
        
