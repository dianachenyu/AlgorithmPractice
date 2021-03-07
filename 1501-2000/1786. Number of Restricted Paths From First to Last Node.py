# Dijkstra + DP
# Time O(ElogV + E) = O(ElogV)
# Space O(E + V)

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        distances = dict()
        heap = []
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        heap = [(0, n)] # (dis, node)
        while heap:
            dis, node = heapq.heappop(heap)
            if node in distances:
                continue
            distances[node] = dis
            for nnode, weight in graph[node]:
                if nnode not in distances:
                    heapq.heappush(heap, (dis + weight, nnode))
        
        MOD = 10**9 + 7
        
        @functools.lru_cache(n)
        def dfs(node):
            if node == 1:
                return 1
            count = 0
            for nnode, _ in graph[node]:
                if distances[node] < distances[nnode]:
                    count += dfs(nnode)
            return count 
        return dfs(n) % MOD
        
