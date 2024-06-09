class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = collections.defaultdict(int)
        res = 0
        for char in s:
            counter[char] += 1
            res += counter[char]
        return res

