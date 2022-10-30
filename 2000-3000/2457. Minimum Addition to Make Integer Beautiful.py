class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def count(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total
        
        res = 0
        mod = 10
        while count(n) > target:
            diff = mod - n % mod
            res += diff
            n += diff
            mod *= 10
        return res 
