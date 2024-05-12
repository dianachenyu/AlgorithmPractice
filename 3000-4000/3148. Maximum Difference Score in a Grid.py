class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = float('-inf')
       
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp = [grid[0][0]] * n
                elif j == 0:
                    res = max(res, grid[i][0] - dp[0])
                    dp[0] = min(dp[0], grid[i][0])
                else:
                    res = max(res, grid[i][j] - min(dp[j], dp[j-1]))
                    dp[j] = min(dp[j], dp[j-1], grid[i][j])
        return res
         

# DP
# DP[j] represent the minimum value in grid[i][j] and its top-left. Compress 2D DP into 1D DP.      
