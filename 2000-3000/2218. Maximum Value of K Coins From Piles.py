class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:        
        @functools.lru_cache(None)
        def dp(idx, k):
            if k == 0:
                return 0
            if idx == len(piles):
                return float('-inf')
            
            res = dp(idx + 1, k)
            pile = piles[idx]
            val = 0
            for j in range(min(len(pile), k)):
                val += pile[j]
                res = max(res, val + dp(idx + 1, k - j - 1))
            return res 
        
        return dp(0, k)
      
# Time O(nkl)= O(km), n = len(piles), l = avg length of piles, m = total length of piles
# Space O(nk)
