class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        res = -1
        rank = collections.defaultdict(int)
        
        def dfs(node, dis):
            nonlocal res, rank 
            if node == -1 or rank[node] == -1: # end of path or visited
                return
            
            if rank[node] > 0: # same path
                res = max(res, dis - rank[node])
                return
            
            rank[node] = dis
            dfs(edges[node], dis + 1)
            rank[node] = -1 # unset to represent visited 
        
        for node in range(n):
            dfs(node, 1)
        return res 
