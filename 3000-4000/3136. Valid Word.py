class Solution:
    def isValid(self, word: str) -> bool:
        VOWELS = 'aeiou'
        SPECIAL = '@#$'

        if len(word) < 3:
            return False
        word = word.lower()
        has_vowel = False
        has_consonant = False
        for char in word:
            if char in SPECIAL:
                return False
            if char.isalpha():
                if char in VOWELS:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant 
