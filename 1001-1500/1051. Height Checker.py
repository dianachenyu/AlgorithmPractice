# Method 1: Sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(expect!=height for expect, height in zip(expected, heights))


# Method 2: Counting Sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101
        for height in heights:
            counts[height] += 1
        res = 0
        idx = 0
        for height in heights:
            while counts[idx] == 0:
                idx += 1
            res += height != idx
            counts[idx] -= 1
        return res 
