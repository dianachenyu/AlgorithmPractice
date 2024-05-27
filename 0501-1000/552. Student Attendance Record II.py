class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = [[0] * 3 for _ in range(2)]
        memo[0][0] = 1

        for _ in range(n):
            memo_next = [[0] * 3 for _ in range(2)]
            for n_absence in [0, 1]:
                for n_consecutive_late in [0, 1, 2]:
                    # 'P'
                    memo_next[n_absence][0] = (memo_next[n_absence][0] + memo[n_absence][n_consecutive_late]) % MOD
                    # 'A'
                    if n_absence < 1:
                        memo_next[n_absence + 1][0] = (memo_next[n_absence + 1][0] + memo[n_absence][n_consecutive_late]) % MOD
                    if n_consecutive_late < 2:
                        memo_next[n_absence][n_consecutive_late + 1] = (memo_next[n_absence][n_consecutive_late + 1] + memo[n_absence][n_consecutive_late]) % MOD
            memo = memo_next
        return sum(sum(count) % MOD for count in memo) % MOD


# Time O(n)
# Space O(1)
