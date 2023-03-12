class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        res = 0
        VOWELS = 'aeiou'
        for word in words[left : right + 1]:
            res += word[0] in VOWELS and word[-1] in VOWELS
        return res 
        
        
