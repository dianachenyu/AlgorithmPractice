# Method 1: DFS
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        counter = collections.defaultdict(collections.Counter)
        for start, end in tickets:
            counter[start][end] += 1
        
        def dfs(airport, ):
            if stop == n:
                return [airport]
            
            for nairport in sorted(counter[airport].keys()):
                if counter[airport][nairport] > 0:
                    counter[airport][nairport] -= 1
                    trip = dfs(nairport, stop + 1)
                    if trip:
                        return [airport] + trip
                    else:
                        counter[airport][nairport] += 1
            return None

        return dfs("JFK", 0)


# Method 2: Eulerian Path
# Eulerian path: Given an undirected or a directed graph, find a path or circuit that passes through each edge exactly once.
# Eulerian path algorithm Time O(E+V)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse=True)
        path = []

        def dfs(node):
            while graph[node]:
                nnode = graph[node].pop()
                dfs(nnode)
            path.append(node)
        
        dfs("JFK")
        return path[::-1]

# Time O(ElogE)
