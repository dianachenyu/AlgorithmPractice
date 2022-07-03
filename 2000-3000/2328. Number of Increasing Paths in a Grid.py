from functools import cache
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j):
            count = 1
            
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                li, lj = i + di, j + dj
                if 0 <= li < m and 0 <= lj < n and grid[li][lj] < grid[i][j]:
                    count += dp(li, lj)
            return count % MOD
                
        return sum(dp(i, j) for i in range(m) for j in range(n)) % MOD
       
        
# Time O(mn)
# Space O(mn)
