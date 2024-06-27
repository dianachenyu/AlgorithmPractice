class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        index = dict()
        res = 0
        start = 0
        for idx, char in enumerate(s):
            if char in index:
                start = max(start, index[char] + 1)
            res += idx - start + 1
            index[char] = idx
        return res 
