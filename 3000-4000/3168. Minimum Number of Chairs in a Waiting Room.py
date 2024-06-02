class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        count = 0
        for char in s:
            if char == 'E':
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res 
