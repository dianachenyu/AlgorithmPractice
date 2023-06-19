# Method 1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = cur = 0
        for g in gain:
            cur += g
            res = max(res, cur)
        return res 


# Method 2: one-liner
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
