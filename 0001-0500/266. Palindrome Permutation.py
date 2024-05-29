class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        return sum(v % 2 for v in counter.values()) < 2
        
