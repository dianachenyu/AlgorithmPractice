class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        res = k % (2 * (n - 1))
        return res if res < n else 2 * (n - 1) - res

