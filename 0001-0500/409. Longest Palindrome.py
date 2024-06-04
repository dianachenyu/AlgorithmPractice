class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        for char, count in counter.items():
            if count % 2 == 0:
                res += count
            else:
                if res % 2 == 0:
                    res += count
                else:
                    res += count - 1
        return res 
