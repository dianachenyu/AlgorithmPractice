class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        num = 0
        
        for idx in range(n):
            if s[n - idx - 1] == '0':
                res += 1
            elif num + (1 << idx) <= k:
                res += 1
                num += 1 << idx
        return res
            
        
