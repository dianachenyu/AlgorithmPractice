class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = collections.defaultdict(set)
        for u,  v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # remove subgraph without coins
        for u in graph:
            while len(graph[u]) == 1 and not coins[u]:
                v = graph[u].pop()
                graph[v].remove(u)
                u = v
        
        # remove leaves, two rounds
        for _ in range(2):
            leaves = [u for u in graph if len(graph[u]) == 1]
            for u in leaves:
                if graph[u]:
                    v = graph[u].pop()
                    graph[v].remove(u)
        return sum(len(nodes) for nodes in graph.values())

      
# Graph
# Time O(N), Space O(N)
