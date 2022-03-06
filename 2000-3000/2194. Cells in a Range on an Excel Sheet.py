class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(col) + str(row) for col in range(ord(s[0]), ord(s[3]) + 1) for row in range(int(s[1]), int(s[4]) + 1)]
