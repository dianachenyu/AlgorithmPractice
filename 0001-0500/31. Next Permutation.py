class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = j = n - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0: # nums are in descending order
            nums.reverse()
            return
        
        k = i - 1
        while nums[j] <= nums[k]: # find the smallest num larger than nums[k]
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        
        # reverse nums[k + 1:]
        left, right = k + 1, n -1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
# Time O(n)
# Space O(1)
                    
        
