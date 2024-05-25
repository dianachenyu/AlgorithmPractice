class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = set(wordDict)

        @cache
        def dp(i):
            if i == n:
                return True
            for ni in range(i + 1, n + 1):
                word = s[i: ni]
                if word in d and dp(ni):
                    return True
            return False

        return dp(0)

      
# n=len(s), m=len(wordDict), k=average length of the words in wordDict
# Time O(nmk)
# Space O(n)
