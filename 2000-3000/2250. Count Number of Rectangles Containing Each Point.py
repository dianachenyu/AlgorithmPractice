class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        by_heights = collections.defaultdict(list)
        for l, h in rectangles:
            by_heights[h].append(l)
        heights = sorted(list(by_heights.keys()), reverse=True)
        for h in heights:
            by_heights[h].sort()
        
        res = []
        
        def calculate(x, y):
            count = 0
            for h in heights:
                if h < y:
                    break
                x_idx = bisect.bisect_left(by_heights[h], x)
                count += len(by_heights[h]) - x_idx
            return count
        
        for x, y in points:
            res.append(calculate(x, y))
        return res
        
