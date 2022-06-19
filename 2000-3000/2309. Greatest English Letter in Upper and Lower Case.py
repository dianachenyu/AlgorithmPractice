class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for char in string.ascii_uppercase[::-1]:
            if char in s and char.lower() in s:
                return char
        return ''
                
        
