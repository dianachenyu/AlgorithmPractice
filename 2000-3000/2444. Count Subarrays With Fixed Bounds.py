class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = min_idx = max_idx = -1

        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_idx = idx
                continue
            if num == minK:
                min_idx = idx
            if num == maxK:
                max_idx = idx
            count = max(0, min(min_idx, max_idx) - bad_idx)
            res += count
        return res
     
    
# Three pointers
# Time O(n), Space O(1)
