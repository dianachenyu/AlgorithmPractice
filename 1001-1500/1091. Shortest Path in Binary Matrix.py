class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        length = 0
        visited = set()
        queue = set([(0, 0)])
        
        while queue:
            nqueue = set()
            length += 1
            for i, j in queue:
                if grid[i][j] != 0 or (i, j) in visited:
                    continue
                if i == n - 1 and j == n - 1:
                    return length 
        
                visited.add((i, j))
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),(-1, 1), (-1, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0 and(ni, nj) not in visited:
                        nqueue.add((ni, nj))
            queue = nqueue
        return -1
