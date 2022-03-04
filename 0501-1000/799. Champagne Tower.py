class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 1)
        dp2 = [0.0] * (query_row + 1)
        dp[0] = poured
    
        for row in range(1, query_row + 1):
            dp2[0] = max(dp[0] - 1, 0.0) / 2 
            for col in range(1, row):
                dp2[col] += max(dp[col - 1] - 1, 0.0) / 2
                dp2[col] += max(dp[col] - 1, 0.0) / 2

            dp2[row] = max(dp[row - 1] - 1, 0.0) / 2 
            dp = copy.copy(dp2)
            dp2 = [0.0] * (query_row + 1)

        return min(dp[query_glass], 1.0)
    
                    
