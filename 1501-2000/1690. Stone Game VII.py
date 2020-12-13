# Time O(n^2)
# Space O(n^2)

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        presum = [0]*(n+1)

        for idx in range(len(stones)):
            presum[idx+1] = presum[idx] + stones[idx]

        @functools.lru_cache(None)
        def dp(l, r):
            if l == r:
                return 0 
     
            left = presum[r+1] - presum[l+1] - dp(l+1, r)
            right = presum[r] - presum[l] - dp(l, r-1)
            
            return max(left, right)
        
        res = dp(0, n-1)
        dp.cache_clear()
        return res 
