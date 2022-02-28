class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            res += pref == word[: len(pref)]
        return res 
        
