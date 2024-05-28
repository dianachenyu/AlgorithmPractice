class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:       
        m = len(grid)
        n = len(grid[0])
        distances = collections.defaultdict(int)
        n_buildings = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # BFS from a building 
                    queue = [(i, j, 0)]
                    while queue:
                        nqueue = []
                        for (ii, jj, dis) in queue:
                            dis += 1
                            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                ni = ii + di
                                nj = jj + dj
                                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == -n_buildings:
                                    grid[ni][nj] -= 1
                                    distances[(ni, nj)] += dis
                                    nqueue.append((ni, nj, dis))
                        queue = nqueue
                    n_buildings += 1
        
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -n_buildings:
                    res = min(res, distances[(i, j)])
        return res if res != float('inf') else -1


# BFS
# M=len(grid), N=len(grid[0])
# Time: O(M^2*N^2)
# Space O(MN)

