class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appear = set()
        for char in s:
            if char in appear:
                return char
            appear.add(char)
