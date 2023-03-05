class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        types.sort(key=lambda x:-x[1])       
        MOD = 10 ** 9 + 7

        @functools.cache
        def dfs(total, idx):
            if total == 0:
                return 1
            if idx >= len(types):
                return 0

            count, mark = types[idx]
            res = 0
            for c in range(0, min(total//mark, count) + 1):
                res += dfs(total - c * mark, idx + 1)
            return res % MOD
            
        return dfs(target, 0)
      
      
# Time O(target * n * count), Space O(target * n)
# Knapsack problem
