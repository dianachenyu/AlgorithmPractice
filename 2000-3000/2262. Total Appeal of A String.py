# Method 1: DP
# DP[i] represents the total appeal of susbstrings ending at index i
class Solution:
    def appealSum(self, s: str) -> int:      
        dp = [0] * len(s)
        index = {char: -1 for char in string.ascii_lowercase}
      
        for i, char in enumerate(s):
            dp[i] = (dp[i - 1] if i - 1 >= 0 else 0) + i - index[char]
            index[char] = i
        return sum(dp)
      
# Time O(n)
# Space O(n)


# Method 2: DP
class Solution:
    def appealSum(self, s: str) -> int:     
        res = 0
        count = 0
        index = dict()
        
        for i, char in enumerate(s):
            count += i - (index[char] if char in index else -1)
            res += count
            index[char] = i
        return res

# Time O(n)
# Space O(1)
