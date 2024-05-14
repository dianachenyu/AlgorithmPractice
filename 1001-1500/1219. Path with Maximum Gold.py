class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid),len(grid[0])
        
        def dfs(i, j, step):
            if grid[i][j] == 0 or step > 25:
                return 0
            
            gold = grid[i][j]
            grid[i][j] = 0
            total = 0
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    total = max(total, dfs(ni, nj, step + 1))
            total += gold
            grid[i][j] = gold
            return total 
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, 0))
        return res 

      
# Time O(MN)^2
# Space O(MN)
