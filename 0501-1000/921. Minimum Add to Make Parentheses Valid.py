class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = count = 0
        for char in s:
            if char == '(':
                count += 1
            else:
                if count == 0:
                    res += 1
                else:
                    count -= 1
        res += count
        return res

