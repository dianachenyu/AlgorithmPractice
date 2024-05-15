class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(set)
        for u, v in prerequisites:
            graph[u].add(v)
        n = len(queries)
        res = [False] * n

        @cache
        def dfs(u, v):
            if u == v:
                return True
            for nnode in graph[u]:
                if dfs(nnode, v):
                    return True
            return False
        
        for idx, (u ,v) in enumerate(queries):
            res[idx] = dfs(u, v)
        return res 
