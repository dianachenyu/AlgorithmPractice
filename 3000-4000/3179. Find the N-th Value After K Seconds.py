class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] * n
        for _ in range(k):
            for idx in range(1, n):
                dp[idx] = (dp[idx] + dp[idx - 1]) % MOD
        return dp[-1]

