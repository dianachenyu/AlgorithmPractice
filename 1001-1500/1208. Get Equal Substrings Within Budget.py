# Sliding Window
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = 0
        i = 0 
        for j in range(n):
            cost += abs(ord(s[j]) - ord(t[j]))
            if cost > maxCost:
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1
