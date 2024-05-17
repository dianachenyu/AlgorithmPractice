# Method 1: DFS + coloring
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sizes = {0: 0, 1: 0}
        color = 2 

        def move(i, j):
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    yield ni, nj

        def dfs(i, j, color):
            if not grid[i][j] == 1:
                return 0  

            grid[i][j] = color
            count = 1
            for ni, nj in move(i, j):
                count += dfs(ni, nj, color)
            return count 

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[color] = dfs(i, j, color)
                    color += 1

        res = max(sizes.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    total = 1
                    colors = set([grid[ni][nj] for ni, nj in move(i, j)])
                    total += sum([sizes[color] for color in colors])
                    res = max(res, total)
        return res

# Time O(N^2)
# Space O(N^2)


# Method 2: Union Find
class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(int)
    
    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.size[i] += 1
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            self.parent[max(pi, pj)] = self.parent[min(pi, pj)]
            self.size[min(pi, pj)] += self.size[max(pi, pj)]
            self.size[max(pi, pj)] = 0


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    uf.find((i, j))
                    if i > 0 and grid[i - 1][j]:
                        uf.union((i, j), (i - 1, j))
                    if i + 1 < n and grid[i + 1][j]:
                        uf.union((i, j), (i + 1, j))
                    if j > 0 and grid[i][j - 1]:
                        uf.union((i, j), (i, j - 1))
                    if j + 1 < n and grid[i][j + 1]:
                        uf.union((i, j), (i, j + 1))

        if not uf.size:
            return 1
        res = max(uf.size.values())
        
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    ps = set()
                    if i > 0 and grid[i - 1][j]:
                        ps.add(uf.find((i - 1, j)))
                    if i + 1 < n and grid[i + 1][j]:
                        ps.add(uf.find((i + 1, j)))
                    if j > 0 and grid[i][j - 1]:
                        ps.add(uf.find((i, j -1)))
                    if j + 1 < n and grid[i][j + 1]:
                        ps.add(uf.find((i, j + 1)))
                    total = sum([uf.size[(p, q)] for (p, q) in ps])
                    total += 1
                    res = max(res, total)
        return res


# Time O(N^2)
# Space O(N^2)
# Similar idea as method 1, Longer implementation 
