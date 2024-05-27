class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        counts = [0] * (n + 1)
        for num in nums:
            counts[min(n, num)] += 1
        count = 0
        for i in range(n, -1, -1):
            count += counts[i]
            if i == count:
                return i
        return -1


# Note: bucket sort method works with the constraint 0 <= nums[i] 
# Time O(N)
# Space O(N)
