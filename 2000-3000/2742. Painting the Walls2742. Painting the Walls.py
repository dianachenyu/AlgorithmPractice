# Method 1
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(time)
        pairs = sorted(zip(time, cost), reverse=True)
        
        @cache
        def dp(idx, count):
            if count >= n:
                return 0
            if idx == n:
                return float('inf')
        
            t, c = pairs[idx]
            return min(dp(idx + 1, count), c + dp(idx + 1, count + 1 + t))
            
        return dp(0, 0)

      
# Knapsack DP
# Time O(N^2), Space O(N^2)


# Method 2
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(time)
        dp = [0] + [float('inf')] * n
        
        for c, t in zip(cost, time):
            for i in range(n, 0, -1): # note: i from large to small filling out DP. reverse use current dp results in the current filling
                dp[i] = min(dp[i], dp[max(0, i - t - 1)] + c)
        return dp[n]

      
# Time O(N^2), Space O(N)
