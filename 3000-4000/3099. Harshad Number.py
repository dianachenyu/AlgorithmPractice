class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res = 0
        y = x
        while y:
            res += y % 10
            y //= 10
        return res if x % res == 0 else -1
