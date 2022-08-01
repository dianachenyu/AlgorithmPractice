class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_dist(node):
            dist = dict()
            
            def dfs(node, dis):
                nonlocal dist
                if node in dist or node == -1:
                    return
                dist[node] = dis
                dfs(edges[node], dis + 1)
            
            dfs(node, 0)
            return dist
        
        dist1 = get_dist(node1)
        dist2 = get_dist(node2)
        res = [float('inf'), -1]
        
        for node in dist1:
            if node in dist2:
                d = max(dist1[node], dist2[node])
                if d < res[0] or (d == res[0] and node < res[1]):
                    res = [d, node]
        return res[1]
