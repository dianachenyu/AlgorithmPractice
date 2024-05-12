class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        idx_s = dict()
        for idx, char in enumerate(s):
            idx_s[char] = idx
        res = 0
        for idx, char in enumerate(t):
            res += abs(idx - idx_s[char])
        return res
