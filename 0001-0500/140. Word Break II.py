class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []
        d = set(wordDict)

        def dfs(i, sentence):
            if i == n:
                res.append(' '.join(sentence))
                return 
            for ni in range(i + 1, n + 1):
                if s[i: ni] in d:
                    sentence.append(s[i: ni])
                    dfs(ni, sentence)
                    sentence.pop()
        dfs(0, [])
        return res

      
# Return all possible combinations. At most 2^N combinations. Need to check and potentially return all combos. DP efficiency is the same as Bruce force/backtrack/dfs.
# n=len(s), m=len(wordDict), k=average length of the words in wordDict
# Time O(2^n*mk)
# Space O(2^n*n)
