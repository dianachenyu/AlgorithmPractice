# Method 1:
# Time O(n^2)
# Space O(n^2)

from collections import defaultdict
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cub in cuboids:
            cub.sort()
        cuboids.append([1000, 1000, 1000])
        graph = defaultdict(set)
        n = len(cuboids)
       
        for i in range(n):
            wi, li, hi = cuboids[i]
            for j in range(n):
                if i == j:
                    continue 
                wj, lj, hj = cuboids[j]
                if wj <= wi and lj <= li and hj <= hi:
                    if wj == wi and lj == li and hj == hi and i > j:
                        continue
                    graph[i].add(j)
             
        @functools.lru_cache(None)
        def dfs(node):
            sumh = 0
            for nnode in graph[node]:
                sumh = max(sumh, dfs(nnode))
            h = cuboids[node][2]
            return sumh+h
        return dfs(n-1) - 1000


# Method 2:
# from lee215
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/discuss/970293/JavaC%2B%2BPython-DP-Prove-with-Explanation
# Time O(n^2)
# Space O(n)


class Solution:
    def maxHeight(self, A: List[List[int]]) -> int:
        A = [[0, 0, 0]] + sorted(map(sorted, A))
        dp = [0] * len(A)
        
        for j in range(1, len(A)):
            for i in range(j):
                if all(A[i][k] <= A[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)
        
