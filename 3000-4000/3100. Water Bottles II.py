class Solution:
    def maxBottlesDrunk(self, numBottles: int, exchange: int) -> int:
        res = 0
        full = numBottles
        empty = 0
        while full:
            res += full
            empty += full
            full = 0
            if empty >= exchange:
                empty -= exchange
                full += 1
                exchange += 1
        return res 
