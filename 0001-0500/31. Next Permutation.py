class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        p = n - 2
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1
        if p == -1:
            return reverse(nums, 0, n - 1) 

        q = n - 1
        while q >= 0 and nums[q] <= nums[p]:
            q -= 1

        nums[p], nums[q] = nums[q], nums[p]
        reverse(nums, p + 1, n - 1)

        
# Time O(n)
# Space O(1)
                    
        
