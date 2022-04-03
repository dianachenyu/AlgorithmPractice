class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        
        def check(num):
            count = 0
            for candy in candies:
                count += candy // num
            
        
        left, right = 1, total // k
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return right if check(right) else left
        
        
