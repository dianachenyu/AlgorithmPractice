class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] - nums[0] - mid < k:
                left = mid
            else:
                right = mid - 1
        
        if left + 1 == right:
            if nums[right] - nums[0] - right < k:
                left = right
        return nums[0] + k + left


      
# Find the number of missing numbers within [nums[0], nums[i]]:
  # (nums[i] - nums[0] + 1) - (i + 1) = nums[i] - nums[0] - i
# Find the rightmost index i, which has less than k missing numbers -> using binary search
# Find Kth missing element: 
      # nums[0] - 1 + (i + 1 + k) = nums[0] + i + k
