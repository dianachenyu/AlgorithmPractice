# Method 1
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        prev = -1
        for idx in range(len(heights) - 1, -1, -1):
            h = heights[idx]
            if h > prev:
                res.append(idx)
                prev = h
        return res[::-1] 


# Method 2: Mono Stack
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for idx, h in enumerate(heights):
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(idx)
        return stack
