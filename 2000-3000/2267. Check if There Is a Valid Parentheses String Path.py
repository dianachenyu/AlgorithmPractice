class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        @functools.lru_cache(None)
        def dfs(i, j, count):
            if i >= m or j >= n:
                return False
            
            if grid[i][j] == "(":
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False
            
            if i == m - 1 and j == n - 1:
                return count == 0
            
            return dfs(i + 1, j, count) or dfs(i, j + 1, count)
            
        return dfs(0, 0, 0)
  
  
  
# Time O(MN(M+N))
# Space O(MN(M+N))
