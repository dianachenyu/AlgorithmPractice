class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        neighbors = collections.defaultdict(set)
        MOD = 10 ** 9 + 7
        for i in range(n):
            for j in range(n):
                if i != j and nums[j] % nums[i] == 0:
                    neighbors[i].add(j)
                    neighbors[j].add(i)
        
        @cache
        def dfs(visited, last):
            if visited == (1 << n) - 1:
                return 1
            
            res = 0
            if visited == 0:
                curs = list(range(n))
            else:
                curs = neighbors[last]
            
            for cur in curs:
                digit = 1 << cur
                if not visited & digit:
                    visited |= digit
                    res += dfs(visited, cur)
                    visited ^= 1 << cur
            return res % MOD
        
        return dfs(0, -1)

      
# DP + Bitmask
# Time (2^n + n), Space O(n*n + n) = O(n*n)
