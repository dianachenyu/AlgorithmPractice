class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(max_sum):
            sm, count = 0, 1
            for num in nums:
                sm += num
                if sm > max_sum:
                    sm = num
                    count += 1
            return count <= m
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left 
    
    
# Time O(nlogsum), n = len(nums)
# Space O(1)
# Note: non-negative numbers is an important limitation. if any numbers, binary search will not work.
