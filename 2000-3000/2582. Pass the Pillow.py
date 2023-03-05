class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        MOD = 2 * (n - 1)
        idx = time % MOD
        idx = min(idx, MOD - idx)
        return idx + 1

      
# Time O(1), Space O(1)
